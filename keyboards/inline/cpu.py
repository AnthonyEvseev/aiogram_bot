from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_callback, other_callback


razer = InlineKeyboardMarkup(text='razer',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))


button_gru = InlineKeyboardMarkup(text='GPU',
                                   callback_data=buy_callback.new(item_name='GPU', quantity=1))


button_motherboard = InlineKeyboardMarkup(text='Motherboard',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))


button_ram = InlineKeyboardMarkup(text='RAM',
                                   callback_data=buy_callback.new(item_name='CPU', quantity=1))




choice_cpu = InlineKeyboardMarkup(row_width=2)
choice_cpu.insert(razer).insert(button_gru).insert(button_ram).insert(button_motherboard)