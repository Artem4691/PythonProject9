import asyncio
import random
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode


TOKEN = "My Token"


bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(Command("time"))
async def cmd_time(message: types.Message):

    now = datetime.now()

    formatted_time = now.strftime("%d.%m.%Y %H:%M")
    await message.answer(f"Сейчас: {formatted_time}")



@dp.message(Command("random"))
async def cmd_random(message: types.Message):

    random_number = random.randint(1, 100)
    await message.answer(f"Твоё случайное число: {random_number}")



@dp.message(Command("joke"))
async def cmd_joke(message: types.Message):

    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25.",
        "В мире есть 10 типов людей: те, кто понимают двоичную систему, и те, кто нет.",
        "Искал шутку про программистов, но у меня вылетела ошибка 404.",
        "Программист ставит два стакана на тумбочку: один с водой (если захочет пить), другой пустой (если не захочет).",
        "— Папа, а почему солнце встает на востоке и садится на западе? — Работает? Не трогай!"
    ]

    random_joke = random.choice(jokes)
    await message.answer(random_joke)



@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)



async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
