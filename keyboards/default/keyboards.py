from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_buy = KeyboardButton('🛒 Buy')
button_subscribe = KeyboardButton('♡ Subscribe')
button_info = KeyboardButton('Help !')
button_history = KeyboardButton('📖 Histiry')



greed_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(button_buy,button_subscribe).add(button_info,button_history)
