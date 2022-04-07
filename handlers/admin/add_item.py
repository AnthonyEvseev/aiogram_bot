from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_admin
from configs.config import ADMINS


# По команде "add" админ добавляет товар в базу бота

class Admin_bot(StatesGroup):
    item_id = State()
    name = State()
    discription = State()
    price = State()
    amount = State()
    img_item = State()


@dp.message_handler(text="➕ Add", states=None)
async def cm_start(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            await bot.send_message(message.chat.id, "Введите название продукта")
            await Admin_bot.name.set()
        else:
            await state.finish()
            await message.reply('У Вас нет прав администратора')


@dp.message_handler(state='*', commands='cansel')
@dp.message_handler(Text(equals='cansel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ввод данных прекращён.')


@dp.message_handler(state=Admin_bot.name)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['name'] = message.text
            await Admin_bot.next()
            await message.reply('Введите описание')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(state=Admin_bot.discription)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['discription'] = message.text
            await Admin_bot.next()
            await message.reply('Введите цену')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['price'] = message.text
            await Admin_bot.next()
            await message.reply('Введите количество товара на складе')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(state=Admin_bot.amount)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['amount'] = message.text
            await Admin_bot.next()
            await message.reply('Добавьте изображение')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(content_types=['photo'], state=Admin_bot.img_item)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['img_item'] = message.photo[0].file_id
            await message.reply('Данные сохранены')
            await sql_admin.sql_add_command(state)
            await state.finish()
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")
