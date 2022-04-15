from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_buy = KeyboardButton('🍴 Menu')
button_subscribe = KeyboardButton('♡ Subscribe')
button_base = KeyboardButton('🛒 Cart')
button_info = KeyboardButton('❗ Info')

mane_menu = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="")
mane_menu.add(button_buy, button_subscribe).add(button_base, button_info)

