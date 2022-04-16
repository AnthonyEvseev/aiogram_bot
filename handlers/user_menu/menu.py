from loader import dp, bot
from aiogram import filters, types
from data_base import sql_admin


def generate_kb(current_amount):
    current_amount = int(current_amount)

    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    keyboard_markup.add(
        types.InlineKeyboardButton('-', callback_data='counter_{}'.format(current_amount - 1)),
        types.InlineKeyboardButton('{} шт'.format(current_amount), callback_data='empty?'),
        types.InlineKeyboardButton('+', callback_data='counter_{}'.format(current_amount + 1)),
        types.InlineKeyboardButton('Добавить в корзину', callback_data='cart_add'),
    )

    return keyboard_markup


@dp.message_handler(text="🍴 Menu")
async def button_base(message: types.Message):
    read_db = await sql_admin.sql_read_store_menu()
    kb = generate_kb(0)
    for ret in read_db:
        await bot.send_photo(message.from_user.id, ret[5],
                             f'{ret[1]}\n{ret[2]}\nЦена: {ret[3]}₽', reply_markup=kb)


@dp.callback_query_handler(filters.Regexp(regexp='^counter_'))
async def update_post(query: types.CallbackQuery):
    current_amount = query.data.split('_')[-1]
    await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id,
                                        reply_markup=generate_kb(current_amount))
