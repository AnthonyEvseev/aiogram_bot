from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, PreCheckoutQuery
from keyboards.keyboards_admin import mane_admin
import data_base.data_base
from configs.config import ADMINS, PAYMENTS_PROVIDER_TOKEN
from loader import dp, bot
from .states import Purchase
import datetime
from keyboards.keyboards_mane import mane_menu
from data_base import data_base
from aiogram.utils.callback_data import CallbackData

db = data_base.DBCommands()

buy_item = CallbackData("buy", "item_id")


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!"
    if message.from_user.id == int(ADMINS):
        text += ('\n'
                 'Чтобы добавить войти в режим админа введи /mod')
    await message.answer(text, reply_markup=mane_menu)


@dp.message_handler(commands="mod")
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


@dp.message_handler(text='🍴 Menu')
async def show_items(message: types.Message):
    all_item = await db.show_items()
    text = ('{name}\n\n'
            '{description}\n\n'
            'Цена: {price}₽\n')
    for item in all_item:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('Купить', callback_data=buy_item.new(item_id=item.id))
        )

        await message.answer_photo(
            photo=item.photo,
            caption=text.format(name=item.name,
                                description=item.description,
                                price=item.price).title(),
            reply_markup=markup
        )


@dp.callback_query_handler(buy_item.filter())
async def buying_item(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    item_id = int(callback_data.get('item_id'))
    await callback.message.edit_reply_markup()
    item = await data_base.Item.get(item_id)
    if not item:
        await callback.message.answer("Такого товара не существует")
        return
    text = ('Введите колличество товара или нажмите /cansel')

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
    # prices = [
    #     types.LabeledPrice(label='Working Time Machine', amount=5750),
    #     types.LabeledPrice(label='Gift wrapping', amount=500),
    # ]
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
                           start_parameter='time-machine-example',
                           payload='HAPPY FRIDAYS COUPON')

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
