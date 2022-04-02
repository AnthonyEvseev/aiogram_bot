from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Админка бота

class Admin_bot(StatesGroup):
    name = State()
    #    discription = State()
    price = State()


@dp.message_handler(commands="Загрузить", states=None)
async def cm_start(message: types.Message):
    await Admin_bot.name.set()
    await message.reply('Напиши название')


@dp.message_handler(state=Admin_bot.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Admin_bot.next()
    await message.reply('Введите название')


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await Admin_bot.next()
    await message.reply('Введите цену')

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

# def register_habdlers_admin(dp: Dispatcher):
#     dp.register_message_handler(button_info, text="text")
#     dp.register_message_handler(cm_start, commands="Загрузить", states=None)
#     dp.register_message_handler(load_name, state=Admin_bot.name)
#     dp.register_message_handler(load_price, state=Admin_bot.price)
