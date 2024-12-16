from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from zeep import CachingClient
import uvicorn
import xml.etree.ElementTree as ET
from datetime import datetime
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/soap/availability")
def check_availability(start_date: str, end_date: str, room_type: str):
    connection = psycopg2.connect(database="hotel_soap", user="postgres", password="", host="localhost", port="5432")
    cursor = connection.cursor()
    query = """SELECT * FROM availability WHERE room_type=%s AND available_date BETWEEN %s AND %s"""
    cursor.execute(query, (room_type, start_date, end_date))
    rooms = cursor.fetchall()
    root = ET.Element("AvailabilityResponse")
    for room in rooms:
        room_elem = ET.SubElement(root, "room")
        ET.SubElement(room_elem, "room_id").text = str(room[0])
        ET.SubElement(room_elem, "room_type").text = room[1]
        ET.SubElement(room_elem, "available_date").text = str(room[2])
        ET.SubElement(room_elem, "status").text = room[3]
    connection.close()
    return ET.tostring(root, encoding='unicode')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)