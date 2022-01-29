from aiogram import types
from loader import dp
from keyboards.inline.inline_gpu import gpu_mane


@dp.callback_query_handler(text="🛒 ASUS")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="ASUS", reply_markup=gpu.gpu)

@dp.callback_query_handler(text="🛒 Gigabyte")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Gigabyte", reply_markup=gpu.gpu)


@dp.callback_query_handler(text="🛒 MSI")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 MSI", reply_markup=gpu.gpu)


@dp.callback_query_handler(text="🛒 Palit")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Palit", reply_markup=gpu.gpu)
