from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from data import config
from aiogram.dispatcher.filters import  Text
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


# Админка бота

class Admin_bot(StatesGroup):
    name = State()
    discription = State()
    price = State()


@dp.message_handler(commands="admin_panel", states=None)
async def cm_start(message: types.Message):
    await Admin_bot.name.set()
    await message.reply('Введите название продукта')


@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(messege: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await messege.reply('Ok')


@dp.message_handler(state=Admin_bot.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Admin_bot.next()
    await message.reply('Введите описание')


@dp.message_handler(state=Admin_bot.discription)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['discription'] = message.text
    await Admin_bot.next()
    await message.reply('Введите цену')


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()
