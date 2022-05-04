from aiogram import types
from aiogram.dispatcher import FSMContext
from configs.config import ADMINS
from loader import dp, bot
from .states import NewItem
from data_base import data_base
from keyboards.keyboards_admin import mane_admin


@dp.message_handler(user_id=ADMINS, text="/cansel", state=NewItem)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Вы отменили ввод')
    await state.reset_state()


@dp.message_handler(user_id=ADMINS, commands="mod")
async def make_changes_command(message: types.Message):
    await bot.send_message(message.chat.id, "Введи команду", reply_markup=mane_admin)


@dp.message_handler(user_id=ADMINS, text="➕ Append")
async def append_name(message: types.Message):
    await message.answer('Введите название товара или нажмите /cansel')
    await NewItem.name.set()


@dp.message_handler(user_id=ADMINS, state=NewItem.name)
async def append_description(message: types.Message, state: FSMContext):
    name = message.text
    item = data_base.Item()
    item.name = name
    await message.answer('Введите описание товара или нажмите /cansel')
    await NewItem.description.set()
    await state.update_data(item=item)


@dp.message_handler(user_id=ADMINS, state=NewItem.description)
async def append_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    description = message.text
    item: data_base.Item = data.get('item')
    item.description = description
    await message.answer('Введите фотографию товара или нажмите /cansel')
    await NewItem.photo.set()
    await state.update_data(item=item)


@dp.message_handler(user_id=ADMINS, state=NewItem.photo, content_types=types.ContentTypes.PHOTO)
async def append_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    item: data_base.Item = data.get('item')
    item.photo = photo
    await message.answer('Введите цену товара или нажмите /cansel')
    await NewItem.price.set()
    await state.update_data(item=item)


@dp.message_handler(user_id=ADMINS, state=NewItem.price)
async def append_price(message: types.Message, state: FSMContext):
    data = await state.get_data()
    item: data_base.Item = data.get('item')
    try:
        price = int(message.text)
    except ValueError:
        await message.answer('Неверное значение, введите число')
        return
    item.price = price
    await state.update_data(item=item)
    await message.answer('Товар удачно создан')
    data = await state.get_data()
    item: data_base.Item = data.get('item')
    await item.create()
    await state.reset_state()

# @dp.message_handler(user_id=ADMINS)
