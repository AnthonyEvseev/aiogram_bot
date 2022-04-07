from aiogram import types
from loader import dp, bot
from configs.config import ADMINS


# Админка бота

@dp.message_handler(commands="mod")
async def make_changes_command(message: types.Message):
    await message.delete()
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            await bot.send_message(message.chat.id, "Введи команду")
        else:
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")
