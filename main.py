import os
import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import Config
from weather import get_weather

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

# Примеры картинок (замените на реальные URL)
PHOTOS = [
    "https://i01.fotocdn.net/s210/13eda5a3c26f54fe/public_pin_l/2669638036.jpg",
    "https://i.pinimg.com/736x/17/88/c6/1788c60267d9e48aff7c266c094f4b0e.jpg",
    "https://live.staticflickr.com/65535/49525034187_241f48d579_b.jpg"
]

# Команда /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("?? Привет! Я бот с прогнозом погоды!\nИспользуй /help для списка команд")

# Команда /help
@dp.message(Command("help"))
async def help_cmd(message: Message):
    help_text = (
        "?? Доступные команды:\n"
        "/start - Начало работы\n"
        "/help - Помощь\n"
        "/weather - Прогноз погоды\n"
        "/photo - Случайная картинка"
    )
    await message.answer(help_text)

# Команда /weather
@dp.message(Command("weather"))
async def weather(message: Message):
    weather_report = await get_weather()
    await message.answer(weather_report)

# Команда /photo
@dp.message(Command("photo"))
async def send_photo(message: Message):
    photo_url = random.choice(PHOTOS)
    await message.answer_photo(photo=photo_url, caption="?? Вот случайная картинка!")

# Реакция на фото
@dp.message(F.photo)
async def react_photo(message: Message):
    responses = [
        "?? Вау, крутое фото!",
        "?? Интересный ракурс...",
        "?? Мне нравится это изображение!"
    ]
    await message.answer(random.choice(responses))

# Ответ на вопрос про ИИ
@dp.message(F.text.lower() == "что такое ии?")
async def ai_definition(message: Message):
    definition = (
        "?? Искусственный интеллект (ИИ) — это область компьютерных наук, "
        "создающая системы, способные выполнять задачи, требующие человеческого интеллекта: "
        "обучение, распознавание образов, принятие решений и т.д."
    )
    await message.answer(definition)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
