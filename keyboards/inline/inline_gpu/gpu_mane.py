from aiogram.types import InlineKeyboardMarkup

asus = InlineKeyboardMarkup(text='ASUS',
                            callback_data='ASUS')

gigabyte = InlineKeyboardMarkup(text='Gigabyte',
                                callback_data='Gigabyte')

msi = InlineKeyboardMarkup(text='MSI',
                           callback_data='Gigabyte')

palit = InlineKeyboardMarkup(text='Palit',
                             callback_data='Palit')

gpu = InlineKeyboardMarkup(row_width=2)
gpu.insert(asus).insert(gigabyte).insert(msi).insert(palit)
