from fastapi import FastAPI  # type: ignore
from schemas import WeatherResponse, CityRequest #type: ignore 
from services import get_weather #type: ignore 

app = FastAPI()

@app.post("/api/weather", response_model=WeatherResponse)
async def fetch_weather(city_request: CityRequest): 
    weather_data = await get_weather(city_request.city)

    return WeatherResponse(
        city=weather_data['name'],
        temperature=weather_data['main']['temp'],
        description=weather_data['weather'][0]['description'],
        humidity=weather_data['main']['humidity']
    )