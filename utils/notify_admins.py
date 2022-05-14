import logging

from aiogram import Dispatcher

from configs.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(ADMINS, "Бот Запущен ✔")
