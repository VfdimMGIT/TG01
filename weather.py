import aiohttp
from config import Config


async def get_weather() -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={Config.CITY}&appid={Config.WEATHER_API_KEY}&units=metric&lang=ru"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data["cod"] != 200:
                return "? Ошибка получения погоды"

            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"?? Погода в {Config.CITY}: {temp}°C\n{description.capitalize()}"
