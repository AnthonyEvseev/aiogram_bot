from aiogram.types import InlineKeyboardMarkup

cpu = InlineKeyboardMarkup(text='CPU',
                           callback_data='CPU')

gpu = InlineKeyboardMarkup(text='GPU',
                           callback_data='GPU')

ram = InlineKeyboardMarkup(text='RAM',
                           callback_data='RAM')

motherboard = InlineKeyboardMarkup(text='Motherboard',
                           callback_data='Motherboard')

menu = InlineKeyboardMarkup(row_width=2)
menu.insert(cpu).insert(gpu)#.insert(ram).insert(motherboard)
