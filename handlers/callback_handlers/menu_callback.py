from aiogram import types, filters
from handlers.user_menu.menu import generate_kb
from loader import dp, bot
from data_base import sql_admin
from aiogram.dispatcher.filters import Text


# Отлавливает " - " и  " + " из "Menu"
@dp.callback_query_handler(filters.Regexp(regexp='^counter_'))
async def update_counter(callback: types.CallbackQuery):
    current_amount = callback.data.split('_')[-1]
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                        reply_markup=generate_kb(current_amount))


# # Отлавливает "Добавить в корзину" из "Menu"
# @dp.callback_query_handler(Text(startswith='cart_add_'))
# async def cart_add(callback: types.CallbackQuery):
#     current_amount = callback.data.split('_')[-1]
#     await sql_admin.sql_cart_add(current_amount)


# Отлавливает "delete" из меню администратора
@dp.callback_query_handler(Text(startswith='delete '))
async def callback_delete(callback: types.CallbackQuery):
    await sql_admin.sql_delete_item_store_menu(callback.data.replace('delete ', ''))
    await callback.message.answer(text=f"{callback.data.replace('delete ', '')} удалена")
    await callback.answer()
