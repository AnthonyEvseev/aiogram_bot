from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_buy = InlineKeyboardButton('🛒 Buy', callback_data='buy')
button_subscribe = InlineKeyboardButton('♡ Subscribe')
button_info = InlineKeyboardButton('❗ Help')
button_history = InlineKeyboardButton('📖 Histiry')

greed_kb = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(button_buy,button_subscribe).add(button_info,button_history)
