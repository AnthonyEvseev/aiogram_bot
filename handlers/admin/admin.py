from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from data_base import sql_admin

ID = None


# Админка бота

class Admin_bot(StatesGroup):
    admin_id = State()
    item_id = State()
    name = State()
    discription = State()
    price = State()
    amount = State()
    img_item = State()


@dp.message_handler(commands='admin')
async def check_admin(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['check_admin'] = message.from_user.id
    await message.reply('Проверка админа пройдена')
    await sql_admin.sql_check_admin(state)
    await state.finish()



@dp.message_handler(commands="mod", is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Введи команду")
    await message.delete()
