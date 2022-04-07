from .admin import Admin_bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_admin
from configs.config import ADMINS


# Здесь прописаны хендлеры команд админа
# В кадом херндлере прописана проверка id админа

@dp.message_handler(commands="add", states=None)
async def cm_start(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            await Admin_bot.name.set()
            await message.reply('Введите название продукта')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(state='*', commands='cansel')
@dp.message_handler(Text(equals='cansel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await message.reply('Ok')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(state=Admin_bot.name)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            async with state.proxy() as data:
                data['name'] = message.text
            await Admin_bot.next()
            await message.reply('Введите описание')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(state=Admin_bot.discription)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            async with state.proxy() as data:
                data['discription'] = message.text
            await Admin_bot.next()
            await message.reply('Введите цену')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(state=Admin_bot.price)
async def load_price(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            async with state.proxy() as data:
                data['price'] = message.text
            await Admin_bot.next()
            await message.reply('Введите количество товара на складе')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(state=Admin_bot.amount)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            async with state.proxy() as data:
                data['amount'] = message.text
            await Admin_bot.next()
            await message.reply('Добавьте изображение')
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')


@dp.message_handler(content_types=['photo'], state=Admin_bot.img_item)
async def load_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        try:
            async with state.proxy() as data:
                data['img_item'] = message.photo[0].file_id
            await message.reply('Данные сохранены')
            await sql_admin.sql_add_command(state)
            await state.finish()
        except:
            await state.finish()
            await message.reply('Вы не администратор,\n'
                                'командане выполнена')
