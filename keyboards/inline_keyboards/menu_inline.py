from aiogram.types import InlineKeyboardMarkup

cpu = InlineKeyboardMarkup(text='CPU',
                           callback_data='CPU')

gpu = InlineKeyboardMarkup(text='GPU',
                           callback_data='GPU')

menu = InlineKeyboardMarkup(row_width=2)
menu.insert(cpu).insert(gpu)
