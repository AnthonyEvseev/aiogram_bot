from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data_base import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
PAYMENTS_PROVIDER_TOKEN = config.PAYMENTS_PROVIDER_TOKEN
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
