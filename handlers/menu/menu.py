from loader import dp, bot
from aiogram import types
from data_base import sql_admin
from keyboards.inline_keyboards.menu_inline import menu


@dp.message_handler(text="🍴 Menu")
async def button_base(message: types.Message):
    read_db = await sql_admin.sql_read_store_menu()
    for ret in read_db:
        await bot.send_photo(message.from_user.id, ret[5],
                             f'{ret[1]}\n{ret[2]}\nЦена: {ret[3]}₽', reply_markup=menu)
