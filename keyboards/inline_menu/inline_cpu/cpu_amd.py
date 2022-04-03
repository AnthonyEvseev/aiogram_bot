from aiogram.types import InlineKeyboardMarkup

ryzen_5_3600 = InlineKeyboardMarkup(text='Ryzen 5 3600, OEM - 20500 ₽',
                            callback_data='core_i5_10400_f_box')

athlon_3000g = InlineKeyboardMarkup(text='Athlon 3000G, OEM - 6000 ₽',
                                callback_data='core_i3_10100_f_box')

ryzen_5_5600x = InlineKeyboardMarkup(text='Ryzen 5 5600X, OEM - 20000 ₽',
                           callback_data='core_i5_11400_f_box')

athlon_200GE = InlineKeyboardMarkup(text='Athlon 200GE, OEM - 5000 ₽',
                             callback_data='core_i5_10105_f_box')

cpu_amd = InlineKeyboardMarkup(row_width=1)
cpu_amd.insert(ryzen_5_3600).insert(athlon_3000g)\
    .insert(ryzen_5_5600x).insert(athlon_200GE)
