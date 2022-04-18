from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_admin
from configs.config import ADMINS


# По команде "add" админ добавляет товар в базу бота

class Store_items(StatesGroup):
    item_id = State()
    name = State()
    discription = State()
    price = State()
    img_item = State()


@dp.message_handler(text="➕ Append", states=None)
async def cm_start(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            await bot.send_message(message.chat.id, "Введите название продукта")
            await Store_items.name.set()
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


@dp.message_handler(state=Store_items.name)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['name'] = message.text
            await Store_items.next()
            await message.reply('Введите описание')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(state=Store_items.discription)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['discription'] = message.text
            await Store_items.next()
            await message.reply('Введите цену')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(lambda message: not message.text.isdigit(), state=Store_items.price)
async def process_load_price_invalid(message: types.Message):
    return await message.reply("Цена должна быть числом.\nВведите, пожалуйста, число")


@dp.message_handler(state=Store_items.price)
async def load_price(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['price'] = message.text
            await Store_items.next()
            await message.reply('Добавьте изображение\n\n'
                                'Обязательно поставьте галочку\n'
                                '"Сжать изображение"')
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(content_types=['photo'], state=Store_items.img_item)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            async with state.proxy() as data:
                data['img_item'] = message.photo[0].file_id
            await message.reply('Данные сохранены')
            await sql_admin.sql_append_item_store_menu(state)
            await state.finish()
        else:
            await state.finish()
            await bot.send_message(message.chat.id, "У Вас нет прав администратора")
