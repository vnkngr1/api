from fastapi import APIRouter, HTTPException
from app.models import Country
from app.database import get_connection

router = APIRouter()

@router.get("/countries", response_model=list[Country])
def get_countries():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, population FROM countries")
    rows = cursor.fetchall()
    connection.close()
    return [Country(name=row["name"], population=row["population"]) for row in rows]

@router.post("/countries", response_model=Country)
def add_country(country: Country):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO countries (name, population) VALUES (?, ?)", (country.name, country.population))
        connection.commit()
    except Exception:
        connection.close()
        raise HTTPException(status_code=400, detail="Country already exists")
    connection.close()
    return country