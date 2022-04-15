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


# Отлавливает нажатие на кнопку "🛒 Store"
@dp.message_handler(text="🛒 Basket")
async def button_store(message: types.Message):
    await message.answer(text="🛒 Choose a product category!", reply_markup=menu)


# Отлавливает нажатие на кнопку "❗ Info"
@dp.message_handler(text="❗ Info")
async def button_info(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hellow, Я TonyTestBot 🚀\n"
                           "Для друзей просто Tony 😏\n\n"
                           'После нажатия на кнопку "Store"\n'
                           'откроется интернет магазин,\n'
                           'где ты сможешь сделать заказ 🛒\n\n'
                           "Я пока не закончен, но скоро всё будет 🔥")
