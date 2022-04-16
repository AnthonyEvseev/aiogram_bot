from aiogram import types
from loader import dp
from data_base import sql_admin
from aiogram.dispatcher.filters import Text


@dp.callback_query_handler(Text(startswith='delete '))
async def callback_delete(callback: types.CallbackQuery):
    await sql_admin.sql_delete_item_store_menu(callback.data.replace('delete ', ''))
    await callback.message.answer(text=f"{callback.data.replace('delete ', '')} удалена")
    await callback.answer()
