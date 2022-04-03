from aiogram.types import InlineKeyboardMarkup

asus_1070 = InlineKeyboardMarkup(text='asus_1070 - 30000 ₽',
                                 callback_data='Asus 1070')

asus_1080 = InlineKeyboardMarkup(text='asus_1080 - 35000 ₽',
                                 callback_data='Asus 1080')

gpu_asus = InlineKeyboardMarkup(row_width=1)
gpu_asus.insert(asus_1070).insert(asus_1080)
