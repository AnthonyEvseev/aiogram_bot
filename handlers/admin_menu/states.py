from aiogram.dispatcher.filters.state import StatesGroup, State


class NewItem(StatesGroup):
    category_name = State()
    subcategory_name = State()
    name = State()
    description = State()
    photo = State()
    price = State()


class Purchase(StatesGroup):
    enterquantity = State()
    approval = State()
    payment = State()
    amount = State()


class Mailing(StatesGroup):
    text = State()
