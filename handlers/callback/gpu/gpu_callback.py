from aiogram import types
from loader import dp
from keyboards.inline.inline_gpu import gpu_asus, gpu_msi


@dp.callback_query_handler(text="ASUS")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="ASUS", reply_markup=gpu_asus.gpu_asus)
    await callback.answer()

@dp.callback_query_handler(text="MSI")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 MSI", reply_markup=gpu_msi.gpu_msi)
    await callback.answer()