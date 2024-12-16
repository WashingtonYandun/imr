from fastapi import FastAPI
import psycopg2
import uvicorn

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(database="hotel_inventory", user="postgres", password="@Was!2023", host="localhost", port="5432")

@app.post("/rooms")
def create_room(room_number: int, room_type: str, status: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO rooms (room_number, room_type, status) VALUES (%s, %s, %s)", (room_number, room_type, status))
    connection.commit()
    connection.close()
    return {"message": "Room created"}

@app.patch("/rooms/{id}")
def update_room_status(id: int, status: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE rooms SET status=%s WHERE room_id=%s", (status, id))
    connection.commit()
    connection.close()
    return {"message": "Room status updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)