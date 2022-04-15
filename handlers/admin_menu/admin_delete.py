from aiogram import types
from loader import dp, bot
from data_base import sql_admin
from configs.config import ADMINS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(text='🗑️ Delete')
async def del_item(message: types.Message):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            read = await sql_admin.sql_read_store_menu()
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[5], f"Название товара: {ret[1]}",
                                     reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}',
                                                                                                  callback_data=f'delete {ret[1]}')))
