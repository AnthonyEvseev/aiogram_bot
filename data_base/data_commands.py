from typing import List
from sqlalchemy import and_
from .data_base import Item
from gino import Gino

db = Gino()


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_item(**kwargs):
    new_item = await Item(**kwargs).create()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ категориями
async def get_categories() -> List[Item]:
    return await Item.query.distinct(Item.category_name).gino.all()


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_name).where(Item.category_name == category).gino.all()


# Функция для подсчета товаров с выбранными категориями и подкатегориями
async def count_items(category_name, subcategory_name=None):
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = [Item.category_name == category_name]

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_name:
        conditions.append(Item.subcategory_name == subcategory_name)

    # Функция подсчета товаров с указанными условиями
    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(category_name, subcategory_name) -> List[Item]:
    item = await Item.query.where(
        and_(Item.category_name == category_name,
             Item.subcategory_name == subcategory_name)
    ).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item
