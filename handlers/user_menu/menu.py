from aiogram.utils.callback_data import CallbackData
from loader import dp, bot
from aiogram import types
from data_base import sql_admin
# from data_base.sql_admin import sql_read_store_menu_test


@dp.message_handler(text="🍴 Menu")
async def button_base(message: types.Message):
    await sql_admin.sql_read_store_menu_test(message)

# @dp.message_handler(text="🍴 Menu")
# async def button_base(message: types.Message):
#     read_db = await sql_admin.sql_read_store_menu()
#     kb = generate_kb(0)
#     for ret in read_db:
#         await bot.send_photo(message.from_user.id, ret[4],
#                              f'{ret[1]}\n{ret[2]}\nЦена: {ret[3]}₽', reply_markup=kb)

callback_menu = CallbackData('item', 'item_id', 'amount')


async def make_callback_menu(item_id='0', amount='0'):
    return callback_menu.new(item_id=item_id, amount=amount)


def generate_kb(current_amount, name, item):
    current_amount = int(current_amount)
    # global callback_menu
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    keyboard_markup.add(
        types.InlineKeyboardButton('-', callback_data='counter_{}'.format(current_amount - 1)),
        types.InlineKeyboardButton('{} шт'.format(current_amount), callback_data='empty?'),
        types.InlineKeyboardButton('+', callback_data='counter_{}'.format(current_amount + 1)),
        types.InlineKeyboardButton(f'Добавить в корзину: {name}', callback_data=f'cart_add_{item}'),
        # types.InlineKeyboardButton('Добавить в корзину', callback_data='cart_add_{}'.format(current_amount)),
    )

    return keyboard_markup
