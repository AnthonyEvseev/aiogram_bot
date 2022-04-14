from aiogram.types import InlineKeyboardMarkup

delete = InlineKeyboardMarkup(text='delete ',
                              callback_data='delete ')  # f'delete ret[1]

delete_item = InlineKeyboardMarkup(row_width=3)
delete_item.add(delete)
