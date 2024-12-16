from fastapi import FastAPI, HTTPException
import psycopg2
import uvicorn

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(database="hotel_rest", user="postgres", password="", host="localhost", port="5432")

@app.post("/reservations")
def create_reservation(customer_name: str, room_number: int, start_date: str, end_date: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """INSERT INTO reservations (customer_name, room_number, start_date, end_date, status) VALUES (%s, %s, %s, %s, 'Confirmed') RETURNING reservation_id"""
    cursor.execute(query, (customer_name, room_number, start_date, end_date))
    reservation_id = cursor.fetchone()[0]
    connection.commit()
    connection.close()
    return {"reservation_id": reservation_id}

@app.get("/reservations/{id}")
def get_reservation(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM reservations WHERE reservation_id=%s", (id,))
    reservation = cursor.fetchone()
    connection.close()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {
        "reservation_id": reservation[0],
        "room_number": reservation[1],
        "customer_name": reservation[2],
        "start_date": reservation[3],
        "end_date": reservation[4],
        "status": reservation[5]
    }

@app.delete("/reservations/{id}")
def cancel_reservation(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM reservations WHERE reservation_id=%s", (id,))
    connection.commit()
    connection.close()
    return {"message": "Reservation canceled"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)