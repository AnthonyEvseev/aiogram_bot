from aiogram import executor
from loader import dp
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data_base import data_base


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Включает базу данных
    await data_base.create_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
