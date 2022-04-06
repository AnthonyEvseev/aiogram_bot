from loader import bot
import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('store_data.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    # SQL запрос на создание таблицы 'store_memu'
    base.execute('CREATE TABLE IF NOT EXISTS store_menu(item_id INTEGER PRIMARY KEY,name TEXT, '
                 'discription TEXT, price INTEGER, amount INTEGER, img_item TEXT)')
    # SQL запрос на создание таблицы 'check_admin'
    base.execute('CREATE TABLE IF NOT EXISTS check_admin(admin_id INTEGER PRIMARY KEY, name TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO store_menu VALUES ( NULL, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# async def sql_read(message):
#     for ret in cur.execute('SELECT * FROM store_menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[5], f'ID товара: {ret[0]}\nНазвание товара: {ret[1]}\n'
#                     f'Описание: {ret[2]}\nЦена: {ret[3]}$\nКолличество в наличии: {ret[4]}\n')


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM store_menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[5], f'Название товара: {ret[1]}\n'
                                                           f'Описание: {ret[2]}\nЦена: {ret[3]} ₽\n')
