import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException  # type: ignore

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(f"Loaded API_KEY: {API_KEY}")  # Debugging line to check if API_KEY is loaded
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str) -> dict:
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API_KEY not found")
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
   
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")
        return response.json()