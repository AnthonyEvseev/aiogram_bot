from aiogram import types
from loader import dp
from data_base import sql_admin
from aiogram.dispatcher.filters import Text
from keyboards.inline_keyboards.inline_gpu import gpu_menu
# from keyboards.inline_keyboards.menu_inline import menu
from aiogram.types import InlineKeyboardMarkup

RES = 0


@dp.callback_query_handler(text='like_-1')
async def count_item(callback: types.CallbackQuery):
    global RES
    RES -= 1
    await callback.message.answer(text=f'{RES}')
    await callback.answer()


@dp.callback_query_handler(text='like_1')
async def count_item(callback: types.CallbackQuery):
    global RES
    RES += 1
    await callback.message.answer(text=f'{RES}')
    await callback.answer()


@dp.callback_query_handler(Text(startswith='delete '))
async def callback_delete(callback: types.CallbackQuery):
    await sql_admin.sql_delete_item_store_menu(callback.data.replace('delete ', ''))
    await callback.message.answer(text=f"{callback.data.replace('delete ', '')} удалена")
    await callback.answer()


# Пример старого колбека, на всякий случай
@dp.callback_query_handler(text="GPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=gpu_menu.gpu)
    await callback.answer()


minus = InlineKeyboardMarkup(text='➖',
                             callback_data="like_-1")

counter = InlineKeyboardMarkup(text=f'{RES} шт.',
                               callback_data='test')

plus = InlineKeyboardMarkup(text='➕',
                            callback_data='like_1')

buy = InlineKeyboardMarkup(text='Добавить в корзину',
                           callback_data='buy')

menu = InlineKeyboardMarkup(row_width=3)
menu.add(minus, counter, plus).add(buy)
