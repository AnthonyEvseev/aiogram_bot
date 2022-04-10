from loader import dp, bot
from aiogram import types
from data_base import sql_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(text="🍴 Menu")
async def button_base(message: types.Message):
    read = await sql_admin.sql_read_store_menu()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[5], reply_markup=InlineKeyboardMarkup().
                             add(InlineKeyboardButton(f' - "{ret[1]}"',
                                                      callback_data=f'delete {ret[1]}')))
