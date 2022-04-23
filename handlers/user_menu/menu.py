from loader import dp, bot
from aiogram import types
from data_base import sql_admin


def generate_kb(current_amount):
    current_amount = int(current_amount)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    keyboard_markup.add(
        types.InlineKeyboardButton('-', callback_data='counter_{}'.format(current_amount - 1)),
        types.InlineKeyboardButton('{} шт'.format(current_amount), callback_data='empty?'),
        types.InlineKeyboardButton('+', callback_data='counter_{}'.format(current_amount + 1)),
        types.InlineKeyboardButton('Добавить в корзину',
                                   callback_data='cart_add_{}'.format(current_amount)),
    )
    return keyboard_markup


@dp.message_handler(text="🍴 Menu")
async def store_menu(message: types.Message):
    read_db = await sql_admin.sql_read_store_menu()
    kb = generate_kb(0)
    for ret in read_db:
        await bot.send_photo(message.from_user.id, ret[4],
                             f'{ret[1]}\n{ret[2]}\nЦена: {ret[3]}₽', reply_markup=kb)
