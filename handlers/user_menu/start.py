from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.keyboards_mane import mane_menu
from loader import dp
from configs.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!"
    if message.from_user.id == int(ADMINS):
        text += ('\n'
                    'Чтобы добавить войти в режим админа введи /mod')
    await message.answer(text, reply_markup=mane_menu)
