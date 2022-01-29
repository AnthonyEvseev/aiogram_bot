from aiogram import types
from loader import dp
from keyboards.inline.inline_cpu import cpu_intel, cpu_amd


@dp.callback_query_handler(text="AMD")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select CPU", reply_markup=cpu_amd.cpu_amd)

@dp.callback_query_handler(text="Intel")
async def button_store(callback: types.CallbackQuery):
    await callback.message.answer(text="🛒 Select GPU", reply_markup=cpu_intel.cpu_intel)
