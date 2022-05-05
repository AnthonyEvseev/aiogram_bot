from aiogram import types, Bot
from gino import Gino
from gino import schema
from sqlalchemy import Column, Integer, BigInteger, String, Sequence, TIMESTAMP, BOOLEAN, JSON, sql
from configs.config import BD_USER, BD_PASSWORD, HOST, BD_NAME

db = Gino()


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    referral = Column(Integer)
    queue: sql.Select


class Item(db.Model):
    __tablename__ = "items"
    queue: sql.Select
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    category_name = Column(String(50))
    subcategory_name = Column(String(50))
    name = Column(String(50))
    photo = Column(String(250))
    description = Column(String(400))
    price = Column(Integer)

    def __repr__(self):
        return f"""
Товар №{self.id} - {self.name}
Цена: {self.price}
"""


class Purchase(db.Model):
    __tablename__ = "purchase"
    queue: sql.Select
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    buyer = Column(BigInteger)
    item_id = Column(Integer)
    amount = Column(Integer)
    quantity = Column(Integer)
    purchase_time = Column(TIMESTAMP)
    shipping_address = Column(JSON)
    phone_number = Column(String(50))
    receiver = Column(String(100))
    successful = Column(BOOLEAN, default=False)


class DBCommands:
    async def get_user(self, user_id) -> User:
        user = await User.query.where(User.user_id == user_id).dino.first()
        return user

    async def add_new_user(self, referral=None) -> User:
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name
        if referral:
            new_user.referral = int(referral)
        await new_user.create()
        return new_user

    async def count_user(self):
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referral(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        referrals = await User.query.where(User.referral == user.id).gino.all()
        return ', '.join([
            f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
            for num, referral in enumerate(referrals)
        ])

    async def show_items(self):
        items = await Item.query.gino.all()
        return items


async def create_db():
    await db.set_bind(f'postgresql://{BD_USER}:{BD_PASSWORD}@{HOST}/{BD_NAME}')
    db.gino: schema.GinoSchemaVisitor
    await db.gino.create_all()
