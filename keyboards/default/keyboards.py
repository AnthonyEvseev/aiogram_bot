from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import buy_callback, other_callback

button_buy = KeyboardButton('🛒 Store')
button_subscribe = KeyboardButton('♡ Subscribe')
button_info = KeyboardButton('❗ Info')

#прикреплённая к сооблению клавиатура

# button_subscribe = InlineKeyboardMarkup(text='♡ Subscribe', callback_data=other_callback.new(subscribe='subscribe',quantity=1))
# button_info = InlineKeyboardMarkup('❗ Help')
# button_info_history = InlineKeyboardMarkup('📖 History')

# cancel = InlineKeyboardMarkup(text='❌ cancel', callback_data=buy_callback.new(item_name='cancel', quantity=1))

# greed_kb = InlineKeyboardMarkup(resize_keyboard=True)\
#     .add(button_buy,button_subscribe)#.add(button_info,button_history)

greed_kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="")
greed_kb.add(button_buy, button_subscribe).add(button_info)