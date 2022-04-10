from aiogram.types import InlineKeyboardMarkup

prise = InlineKeyboardMarkup(text='Сумма: ₽',
                           callback_data='none')

minus = InlineKeyboardMarkup(text='➖',
                             callback_data='➖')

none_item = InlineKeyboardMarkup(text='шт.',
                                 callback_data='none')

plus = InlineKeyboardMarkup(text='➕',
                            callback_data='➕')

buy = InlineKeyboardMarkup(text='Добавить в корзину',
                           callback_data='buy')

menu = InlineKeyboardMarkup(row_width=3)
menu.add(prise).add(minus, none_item, plus).add(buy)
