from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_callback, other_callback

button_cpu = InlineKeyboardMarkup(text='CPU',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))




button_gru = InlineKeyboardMarkup(text='GPU',
                                   callback_data=buy_callback.new(item_name='GPU', quantity=1))

button_cpu_ = InlineKeyboardMarkup(text='CPU',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))




choice = InlineKeyboardMarkup(row_width=2)
choice.insert(button_cpu).insert(button_gru)

choice_cpu = InlineKeyboardMarkup(row_width=2)
choice.insert(button_cpu).insert(button_gru)