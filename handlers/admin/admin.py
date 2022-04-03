from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp, bot
from data_base import config
from aiogram.dispatcher.filters import Text
from data_base import sql_admin

ID = None


# Админка бота

class Admin_bot(StatesGroup):
    name = State()
    discription = State()
    price = State()


@dp.message_handler(commands="mod", is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Введи команду")
    await message.delete()


@dp.message_handler(commands="admin_panel", states=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await Admin_bot.name.set()
        await message.reply('Введите название продукта')


@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok')


@dp.message_handler(state=Admin_bot.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await Admin_bot.next()
        await message.reply('Введите описание')


@dp.message_handler(state=Admin_bot.discription)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['discription'] = message.text
        await Admin_bot.next()
        await message.reply('Введите цену')


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        await message.reply('Данные сохранены')
        await sql_admin.sql_add_command(state)
        await state.finish()
