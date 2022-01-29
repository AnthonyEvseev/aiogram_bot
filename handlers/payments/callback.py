from aiogram import Bot
from aiogram import types
from aiogram.types.message import ContentTypes
from data import config
from loader import dp
from keyboards.inline.cpu import cpu
from keyboards.inline.menu import menu


@dp.callback_query_handler(text="🛒 CPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Choose a product category", reply_markup=cpu)
