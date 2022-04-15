from aiogram import types
from aiogram.types.message import ContentTypes
from loader import dp, bot, PAYMENTS_PROVIDER_TOKEN
from aiogram.dispatcher.filters import Text

# ТЕСТОВЫЙ
# ХЕНДЛЕТ
# НЕ
# ЗАБУДЬ
# УДАЛИТЬ
# @dp.message_handler(commands='test')
# async def alarm(message: types.Message):
#     print(type(ADMINS)), print(type(message.from_user.id))


# Цена за товар
prices = [
    types.LabeledPrice(label='Working Time Machine', amount=5750),
    types.LabeledPrice(label='Gift wrapping', amount=500),
]
# Устанавливается цена за доставку
shipping_options = [
    types.ShippingOption(id='instant', title='WorldWide Teleporter').add(types.LabeledPrice('Teleporter', 1000)),
    types.ShippingOption(id='pickup', title='Local pickup').add(types.LabeledPrice('Pickup', 300)),
]


@dp.message_handler(commands=['terms'])
async def cmd_terms(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Thank you for shopping with our demo bot. We hope you like your new time machine!\n'
                           '1. If your time machine was not delivered on time, please rethink your concept of time'
                           ' and try again.\n'
                           '2. If you find that your time machine is not working, kindly contact our future service'
                           ' workshops on Trappist-1e. They will be accessible anywhere between'
                           ' May 2075 and November 4000 C.E.\n'
                           '3. If you would like a refund, kindly apply for one yesterday and we will have sent it'
                           ' to you immediately.')


# @dp.callback_query_handler(Text(startswith='buy '))
@dp.callback_query_handler(text='buy')
async def buy_cpu(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Не использовать реальную карту!\n"
                           "Don't use real card!\n\n"
                           "Используйте тестовую карту!\n"
                           "Use this test card number to pay for your Time Machine!\n\n"
                           '4111 1111 1111 1111\n'
                           '2024/12\n'
                           '123\n'
                           "3-D Secure:'12345678'\n"
                           "\n\nThis is your demo invoice:", parse_mode='Markdown')
    await bot.send_invoice(message.chat.id, title='Working Time Machine',
                           description='Want to visit your great-great-great-grandparents?'
                                       ' Make a fortune at the races?'
                                       ' Shake hands with Hammurabi and take a stroll in the Hanging Gardens?'
                                       ' Order our Working Time Machine today!',
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='rub',
                           photo_url='https://telegra.ph/file/d08ff863531f10bf2ea4b.jpg',
                           photo_height=512,  # !=0/None or picture won't be shown
                           photo_width=512,
                           photo_size=512,
                           is_flexible=True,  # True If you need to set up Shipping Fee
                           prices=prices,
                           start_parameter='time-machine-example',
                           payload='HAPPY FRIDAYS COUPON')


@dp.shipping_query_handler(lambda query: True)
async def shipping(shipping_query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                                    error_message='О, кажется, наши курьеры-собаки сейчас обедают.'
                                                  ' Попробуйте позже!')


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Инопланетяне пытались украсть CVV вашей карты,"
                                                      " но мы успешно защитили ваши учетные данные,"
                                                      " попробуй еще раз заплатить через несколько минут, нужен небольшой отдых..")


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Ура! Спасибо за оплату! Мы обработаем ваш заказ на `{} {}`'
                           ' как можно быстрее! Оставайтесь на связи.'
                           '\n\nИспользуйте /buy еще раз, чтобы получить Машину времени для вашего друга!'.format(
                               message.successful_payment.total_amount / 100, message.successful_payment.currency),
                           parse_mode='Markdown')
