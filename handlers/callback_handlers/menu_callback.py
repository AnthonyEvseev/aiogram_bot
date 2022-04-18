from aiogram import types, filters
from loader import dp, bot
from data_base import sql_admin
from aiogram.dispatcher.filters import Text
from handlers.user_menu.menu import generate_kb


# Отлавливает " - " и  " + " из "Menu"
@dp.callback_query_handler(filters.Regexp(regexp='^counter_'))
async def update_counter(query: types.CallbackQuery):
    current_amount = query.data.split('_')[-1]
    await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id,
                                        reply_markup=generate_kb(current_amount))


# Отлавливает "Добавить в корзину" из "Menu"
@dp.callback_query_handler(filters.Regexp(regexp='^cart_add'))
async def cart_add(query: types.CallbackQuery):
    pass

# Отлавливает "delete" из меню администратора
@dp.callback_query_handler(Text(startswith='delete '))
async def callback_delete(callback: types.CallbackQuery):
    await sql_admin.sql_delete_item_store_menu(callback.data.replace('delete ', ''))
    await callback.message.answer(text=f"{callback.data.replace('delete ', '')} удалена")
    await callback.answer()
