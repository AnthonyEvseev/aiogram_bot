from aiogram.types import InlineKeyboardMarkup

delete = InlineKeyboardMarkup(text=f'Удалить  ret[1]',
                              callback_data=f'delete ret[1]')

delete_item = InlineKeyboardMarkup(row_width=3)
delete_item.add(delete)