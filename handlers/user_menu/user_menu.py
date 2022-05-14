from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, PreCheckoutQuery, Message
from data_base.data_commands import get_item, get_items
from keyboards.keyboards_admin import mane_admin
from configs.config import ADMINS, PAYMENTS_PROVIDER_TOKEN
from loader import dp, bot
from handlers.admin_menu.states import Purchase
import datetime
from keyboards.keyboards_mane import mane_menu
from handlers.admin_menu.callback import categories_keyboard, subcategories_keyboard, items_keyboard, item_keyboard, \
    menu_cd, buy_item
from data_base import data_base
from typing import Union

db = data_base.DBCommands()


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!"
    if message.from_user.id == int(ADMINS):
        text += ('\n'
                 'Чтобы добавить войти в режим админа введи /admin_mod')
    await message.answer(text, reply_markup=mane_menu)


@dp.message_handler(text='🍴 Menu')
async def show_items(message: types.Message):
    await list_categories(message)


@dp.message_handler(commands="admin_mod")
async def make_changes_command(message: types.Message):
    await message.delete()
    if message.from_user.id == int(ADMINS):
        await bot.send_message(message.chat.id, "Введи команду", reply_markup=mane_admin)
    else:
        await bot.send_message(message.chat.id, "У Вас нет прав администратора")


@dp.message_handler(user_id=ADMINS, text="/cansel", state=Purchase)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Вы отменили ввод')
    await state.reset_state()


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)

    markup = await categories_keyboard()

    text = f"Что же захочет купить {message.from_user.full_name} 😏 ?"

    if isinstance(message, Message):
        await message.answer(text, reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)
    await callback.message.edit_text(text="Смотри, что у нас есть", reply_markup=markup)


# Функция, которая отдает уже кнопку Купить товар по выбранному товару
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    # Берем запись о нашем товаре из базы данных
    item = await get_item(item_id)
    text = f"Купи {item.name}"
    await callback.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(buy_item.filter())
async def buying_item(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    item_id = int(callback_data.get('item_id'))
    await callback.message.edit_reply_markup()
    item = await data_base.Item.get(item_id)
    if not item:
        await callback.message.answer("Такого товара не существует")
        return
    text = ('Введите количество товара или нажмите /cansel')

    await callback.message.answer(text)
    await Purchase.enterquantity.set()
    await state.update_data(
        item=item,
        purchase=data_base.Purchase(
            item_id=item_id,
            purchase_time=datetime.datetime.now(),
            buyer=callback.from_user.id
        )
    )


@dp.message_handler(regexp=r"^(\d+)$", state=Purchase.enterquantity)
async def enter_quantity(message: types.Message, state: FSMContext):
    quantity = int(message.text)
    async with state.proxy() as data:
        data["purchase"].quantity = quantity
        item = data.get('item')
        amount = item.price * quantity
        data['purchase'].amount = amount

    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        types.InlineKeyboardButton('Согласен', callback_data='agree'),
        types.InlineKeyboardButton('Изменить', callback_data='change'),
        types.InlineKeyboardButton('Отменить', callback_data='cansel')
    )

    await message.answer(('Вы выбрали товар "{name}",\nв количестве {quantity}, по цене {price}₽ за шт.\n'
                          'Сумма заказа {amount}₽. Вы подтверждаете заказ?').format(quantity=quantity, name=item.name,
                                                                                    price=item.price,
                                                                                    amount=amount), reply_markup=markup)
    await Purchase.approval.set()


@dp.message_handler(state=Purchase.enterquantity)
async def enter_quantity(message: types.Message):
    await message.answer('Нужно ввести число')


@dp.callback_query_handler(text_contains='cansel', state=Purchase)
async def cansel_purchase(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Вы отменили покупку')
    await state.reset_state()


@dp.callback_query_handler(text_contains='change', state=Purchase.approval)
async def chancge_purchase(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Введите количество')
    await Purchase.enterquantity.set()


@dp.callback_query_handler(text_contains='agree', state=Purchase.approval)
async def agree_purchase(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup()
    data = await state.get_data()
    purchase = data.get('purchase')
    item = data.get('item')
    photo = data.get('photo')
    prices = [
        types.LabeledPrice(label=item.name, amount=purchase.amount * 100),
    ]

    await purchase.create()
    await callback.message.answer("Не использовать реальную карту!\n"
                                  "Don't use real card!\n\n"
                                  "Используйте тестовую карту!\n"
                                  "Use this test card number to pay for your Time Machine!\n\n"
                                  '4111 1111 1111 1111\n'
                                  '2024/12\n'
                                  '123\n'
                                  "3-D Secure:'12345678'\n"
                                  "\n\nThis is your demo invoice:", parse_mode='Markdown')

    await bot.send_invoice(chat_id=callback.from_user.id,
                           title=item.name.title(),
                           description=item.description.title(),
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='rub',
                           # photo='https://telegra.ph/file/d08ff863531f10bf2ea4b.jpg',
                           photo_height=512,  # !=0/None or picture won't be shown
                           photo_width=512,
                           photo_size=512,
                           is_flexible=True,  # True If you need to set up Shipping Fee
                           prices=prices,
                           start_parameter=item.name.title(),
                           payload=item.name.title())

    await state.update_data(purchase=purchase)
    await Purchase.payment.set()


@dp.pre_checkout_query_handler(state=Purchase.payment)
async def checkout(quary: PreCheckoutQuery, state: FSMContext):
    await bot.answer_pre_checkout_query(quary.id, True)
    data = await state.get_data()
    purchase: data_base.Purchase = data.get('purchase')
    success = await check_payment(purchase)
    if success:
        await purchase.update(
            success=True,
        ).apply()
        await state.reset_state()
        await bot.send_message(chat_id=quary.from_user.id, text='Спасибо за покупку')

    else:
        await bot.send_message(chat_id=quary.from_user.id, text='Покупка не удалась')


async def check_payment(purchase: data_base.Purchase):
    return True


# Функция, которая обрабатывает ВСЕ нажатия на кнопки в этой менюшке
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    category = callback_data.get("category")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    subcategory = callback_data.get("subcategory")

    # Получаем айди товара, который выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    item_id = int(callback_data.get("item_id"))

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        "0": list_categories,  # Отдаем категории
        "1": list_subcategories,  # Отдаем подкатегории
        "2": list_items,  # Отдаем товары
        "3": show_item  # Предлагаем купить товар
    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )
