from aiogram import types
from loader import dp
from data_base import sql_admin
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup
from keyboards.inline_keyboards.inline_gpu import gpu_menu
from keyboards.inline_keyboards.inline_cpu import cpu_menu

COUNTER_ITEM = 0

@dp.callback_query_handler(Text(startswith='delete '))
async def callback_delete(callback: types.CallbackQuery):
    await sql_admin.sql_delete_item_store_menu(callback.data.replace('delete ', ''))
    await callback.message.answer(text=f"{callback.data.replace('delete ', '')} удалена.")
    await callback.answer()


# надо придумать как записать эти даннвые
@dp.callback_query_handler(text="➖")
async def button_store(callback: types.CallbackQuery):
    global COUNTER_ITEM
    COUNTER_ITEM -= COUNTER_ITEM
    await callback.answer()

# надо придумать как записать эти даннвые
@dp.callback_query_handler(text="➕")
async def button_store(callback: types.CallbackQuery):
    global COUNTER_ITEM
    COUNTER_ITEM += COUNTER_ITEM
    await callback.answer()


@dp.callback_query_handler(text="CPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select CPU", reply_markup=cpu_menu.cpu)
    await callback.answer()


@dp.callback_query_handler(text="GPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=gpu_menu.gpu)
    await callback.answer()
