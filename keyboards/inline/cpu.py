from aiogram.types import InlineKeyboardMarkup

amd = InlineKeyboardMarkup(text='AMD',
                           callback_data='CPU')

intel = InlineKeyboardMarkup(text='Intel',
                             callback_data='Intel')

cpu = InlineKeyboardMarkup(row_width=2)
cpu.insert(amd).insert(intel)
