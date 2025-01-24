from fastapi import FastAPI
from app.routes import countries

app = FastAPI()

# Подключаем маршруты
app.include_router(countries.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Countries API"}