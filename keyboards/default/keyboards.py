from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_apple, subscribe_callback

button_buy = InlineKeyboardMarkup(text='🛒 Buy apple', callback_data=buy_apple.new(item_name='apple', quantity=1))
button_subscribe = InlineKeyboardMarkup(text='♡ Subscribe', callback_data=subscribe_callback.new(quantity=1))
# button_info = InlineKeyboardMarkup('❗ Help')
# button_history = InlineKeyboardMarkup('📖 Histiry')

greed_kb = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(button_buy,button_subscribe)#.add(button_info,button_history)
