from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from aiogram import types


# Админка бота

class Admin_bot(StatesGroup):
    name = State()
    #    discription = State()
    price = State()


@dp.message.handler(commands="Загрузить", states=None)
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


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()
