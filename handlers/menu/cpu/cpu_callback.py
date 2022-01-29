from aiogram import types
from loader import dp
from keyboards.inline.inline_cpu.cpu_intel import cpu_intel


@dp.callback_query_handler(text="AMD")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select CPU", reply_markup=cpu_intel)

@dp.callback_query_handler(text="Intel")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=cpu_intel)
