from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.keyboards.keyboards import greed_kb

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=greed_kb)
