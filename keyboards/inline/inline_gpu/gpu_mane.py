from aiogram.types import InlineKeyboardMarkup

asus = InlineKeyboardMarkup(text='ASUS',
                            callback_data='ASUS')

msi = InlineKeyboardMarkup(text='MSI',
                           callback_data='MSI')

gpu = InlineKeyboardMarkup(row_width=2)
gpu.insert(asus).insert(msi)
