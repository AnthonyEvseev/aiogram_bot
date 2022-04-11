from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.callback_handlers.menu_callback import COUNTER_ITEM

minus = InlineKeyboardMarkup(text='➖',
                             callback_data="➖")

counter = InlineKeyboardMarkup(text='шт.',
                               callback_data='test')

plus = InlineKeyboardMarkup(text='➕',
                            callback_data='➕')

buy = InlineKeyboardMarkup(text='Добавить в корзину',
                           callback_data='buy')

menu = InlineKeyboardMarkup(row_width=3)
menu.add(InlineKeyboardButton(f'Тест', callback_data='test')).add(minus, counter, plus).add(buy)
