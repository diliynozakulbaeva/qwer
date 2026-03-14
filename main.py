import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandStart

import os
from dotenv import load_dotenv
load_dotenv()

menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='salem'), KeyboardButton(text="alem")]
    ],
    resize_keyboard=True
)
token=os.getenv("Token")
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(messege:Message):
    await messege.answer(f"hello {messege.from_user.username}", reply_markup=menu)
@dp.message(Command("help"))
async def help(messege:Message):
    await messege.answer("qanday jardem kerek? ")



async def main():
    print("...")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
