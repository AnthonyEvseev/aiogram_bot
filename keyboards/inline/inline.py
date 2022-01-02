from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_callback, other_callback

button_item = InlineKeyboardMarkup(text='Choose a product category', callback_data=buy_callback.new(item_name='razen_3600', quantity=1))
choice = InlineKeyboardMarkup(row_width=2)
choice.insert(button_item)