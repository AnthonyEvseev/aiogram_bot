from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_append = KeyboardButton('➕ Append')
button_delete = KeyboardButton('🗑️ Delete')
button_start = KeyboardButton('/start')

mane_admin = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="")
mane_admin.add(button_append, button_delete).add(button_start)
