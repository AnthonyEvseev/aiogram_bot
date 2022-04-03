from aiogram.types import InlineKeyboardMarkup

msi_1070 = InlineKeyboardMarkup(text='MSI 1070 - 35000 ₽',
                            callback_data='msi_1080')

msi_1080 = InlineKeyboardMarkup(text='MSI 1080 - 40000 ₽',
                                callback_data='msi_1080')

gpu_msi = InlineKeyboardMarkup(row_width=1)
gpu_msi.insert(msi_1070).insert(msi_1080)
