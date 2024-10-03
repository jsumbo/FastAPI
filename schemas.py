from pydantic import BaseModel # type: ignore

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: int

class CityRequest(BaseModel):
    city: str