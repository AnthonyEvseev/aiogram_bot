from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

amd = InlineKeyboardMarkup(text='AMD',
                           callback_data='CPU')

intel = InlineKeyboardMarkup(text='Intel',
                             callback_data='Intel')

choice_cpu = InlineKeyboardMarkup(row_width=2)
choice_cpu.insert(amd).insert(intel)
