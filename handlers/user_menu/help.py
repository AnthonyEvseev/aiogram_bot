from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, bot
from configs.config import ADMINS

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.delete()
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")

    await message.answer("\n".join(text))

@dp.message_handler(text="❗ Info")
async def button_info(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hellow, Я TonyTestBot 🚀\n"
                           "Для друзей просто Tony 😏\n\n"
                           'После нажатия на кнопку "Store"\n'
                           'откроется интернет магазин,\n'
                           'где ты сможешь сделать заказ 🛒\n\n'
                           "Я пока не закончен, но скоро всё будет 🔥")
    if message.from_user.id == int(ADMINS):
        text = ('\n'
                'Чтобы добавить войти в режим админа введи /admin_mod')
        await message.answer(text)
