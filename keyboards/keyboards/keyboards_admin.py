from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_add = KeyboardButton('➕ Add')
button_delete = KeyboardButton('🗑️ Delete')

mane_admin = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="")
mane_admin.add(button_add, button_delete)
