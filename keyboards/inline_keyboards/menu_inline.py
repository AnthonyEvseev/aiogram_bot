# from aiogram import types

# Похоже удалю этот файл




# from handlers.callback_handlers.all_callback import RES
#
# minus = InlineKeyboardMarkup(text='➖',
#                              callback_data="like_-1")
#
# counter = InlineKeyboardMarkup(text=f'{RES} шт.',
#                                callback_data='test')
#
# plus = InlineKeyboardMarkup(text='➕',
#                             callback_data='like_1')
#
# buy = InlineKeyboardMarkup(text='Добавить в корзину',
#                            callback_data='buy')
#
# menu = InlineKeyboardMarkup(row_width=3)
# menu.add(minus, counter, plus).add(buy)

# def generate_kb(current_amount):
#     current_amount = int(current_amount)
#
#     mane_menu = types.InlineKeyboardMarkup(row_width=3)
#     mane_menu.add(
#         types.InlineKeyboardButton('-', callback_data='counter_{}'.format(current_amount - 1)),
#         types.InlineKeyboardButton('{} шт'.format(current_amount), callback_data='empty?'),
#         types.InlineKeyboardButton('+', callback_data='counter_{}'.format(current_amount + 1)),
#         types.InlineKeyboardButton('Добавить в корзину', callback_data='cart_add'),
#     )
#
#     return mane_menu

