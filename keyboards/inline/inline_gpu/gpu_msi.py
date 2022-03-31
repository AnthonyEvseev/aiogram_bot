from aiogram.types import InlineKeyboardMarkup

core_i5_10400_f_box = InlineKeyboardMarkup(text='core_i5_10400_f_box - 12500 ₽',
                            callback_data='core_i5_10400_f_box')

core_i3_10100_f_box = InlineKeyboardMarkup(text='core_i3_10100_f_box - 7800 ₽',
                                callback_data='core_i3_10100_f_box')

core_i5_11400_f_box = InlineKeyboardMarkup(text='core_i5_11400_f_box - 16500 ₽',
                           callback_data='core_i5_11400_f_box')

core_i5_10105_f_box = InlineKeyboardMarkup(text='core_i5_10105_f_box - 10500 ₽',
                             callback_data='core_i5_10105_f_box')

cpu_intel = InlineKeyboardMarkup(row_width=1)
cpu_intel.insert(core_i5_10400_f_box).insert(core_i3_10100_f_box)\
    .insert(core_i5_11400_f_box).insert(core_i5_10105_f_box)
