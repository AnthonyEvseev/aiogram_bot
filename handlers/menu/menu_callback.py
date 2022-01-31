from aiogram import types
from loader import dp
from keyboards.inline.inline_gpu import gpu_mane
from keyboards.inline.inline_cpu import cpu_mane


@dp.callback_query_handler(text="CPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select CPU", reply_markup=cpu_mane.cpu)
    await callback.answer()


@dp.callback_query_handler(text="GPU")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=gpu_mane.gpu)
    await callback.answer()
#
# @dp.callback_query_handler(text="RAM")
# async def button_store(callback: types.CallbackQuery):
#     await callback.message.answer(text="🛒 Select RAM", reply_markup=menu.ram)
#
#
# @dp.callback_query_handler(text="🛒 Motherboard")
# async def button_store(callback: types.CallbackQuery):
#     await callback.message.answer(text="🛒 Select Motherboard", reply_markup=menu.motherboard)
