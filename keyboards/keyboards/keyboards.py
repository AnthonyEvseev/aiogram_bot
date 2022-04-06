from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_buy = KeyboardButton('🍴 Menu')
button_subscribe = KeyboardButton('♡ Subscribe')
button_base = KeyboardButton('🛒 Basket')
button_info = KeyboardButton('❗ Info')

greed_kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="")
greed_kb.add(button_buy, button_subscribe).add(button_base, button_info)
