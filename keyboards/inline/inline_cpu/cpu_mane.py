from aiogram.types import InlineKeyboardMarkup

amd = InlineKeyboardMarkup(text='AMD',
                           callback_data='AMD')

intel = InlineKeyboardMarkup(text='Intel',
                             callback_data='Intel')

cpu = InlineKeyboardMarkup(row_width=2)
cpu.insert(amd).insert(intel)
