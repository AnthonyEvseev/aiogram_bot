from aiogram import types
from loader import dp
from keyboards.inline_keyboards.inline_gpu import gpu_menu
from keyboards.inline_keyboards.inline_cpu import cpu_menu


@dp.callback_query_handler(text="CPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select CPU", reply_markup=cpu_menu.cpu)
    await callback.answer()


@dp.callback_query_handler(text="GPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=gpu_menu.gpu)
    await callback.answer()
