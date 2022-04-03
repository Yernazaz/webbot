import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi! Write a name of the city ")

@dp.message_handler()
async def get_weather(message: types.Message):

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        current_temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"City: {city}\n"
                            f"Temperature: {current_temp}C°\n"
                            F"Pressure: {pressure} mmhg\n"
                            F"Humidity: {humidity} %\n"
                            F"Wind: {wind} m/s \n"
                            F"Sunrise: {sunrise_time}\n"
                            F"Sunset: {sunset_time}\n"
                            F"***Have a nice day!***")

    except:
        await message.reply("Check the name of city")

if __name__ == '__main__':
    executor.start_polling(dp)


