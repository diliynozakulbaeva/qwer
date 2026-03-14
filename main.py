import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart

import os
from dotenv import load_dotenv
load_dotenv()

menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='salem'), KeyboardButton(text="alem")],
        [KeyboardButton(text="Fanlar")],
    ],
    resize_keyboard=True
)

fanlar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Algebra', callback_data="algebra"),
            InlineKeyboardButton(text='Geometriya', callback_data="geometriya")
        ],
        [
            InlineKeyboardButton(text='Fizika', callback_data="fizika"),
            InlineKeyboardButton(text='Kimyo', callback_data="kimyo")
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data="back")
        ]
    ]
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

@dp.message(Command('yordam'))   
async def yordam(message: Message):
    await message.answer("sizga qandayyordam kerak?")

@dp.message()
async def menular(message: Message):
    t = message.text
    if t == 'Fanlar':
        await message.answer(f"tanlang ", reply_markup=fanlar_menu)


async def main():
    print("...")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
