from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_callback, other_callback
# from cpu import choice_cpu

button_cpu = InlineKeyboardMarkup(text='🛒 CPU',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))




button_gru = InlineKeyboardMarkup(text='GPU',
                                   callback_data=buy_callback.new(item_name='GPU', quantity=1))


button_motherboard = InlineKeyboardMarkup(text='Motherboard',
                                   callback_data=buy_callback.new(item_name='Motherboard', quantity=1))


button_ram = InlineKeyboardMarkup(text='RAM',
                                   callback_data=buy_callback.new(item_name='RAM', quantity=1))




choice = InlineKeyboardMarkup(row_width=2)
choice.insert(button_cpu).insert(button_gru).insert(button_ram).insert(button_motherboard)