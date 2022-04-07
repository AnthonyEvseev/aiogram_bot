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
    # base.execute('CREATE TABLE IF NOT EXISTS check_admin(admin_id INTEGER PRIMARY KEY)')
    base.commit()


# Записывает результат проверки на админа в БД
# async def sql_check_admin(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO check_admin VALUES ( ?)', tuple(data.values()))
#         base.commit()


# Записывает меню введенное админом в чате
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO store_menu VALUES ( NULL, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# Запрашиваю данные из БД перед возможным удалением
async def sql_read_delete():
    return cur.execute('SELECT * FROM store_menu').fetchall()


# Запрос на удалиение
async def sql_delete(data):
    return cur.execute('DELETE FROM store_menu WHERE name == ?', (data,)), base.commit()


# Вывод меню
async def sql_read_store_menu(message):
    for ret in cur.execute('SELECT * FROM store_menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[5], f'Название товара: {ret[1]}\n'
                                                           f'Описание: {ret[2]}\nЦена: {ret[3]} ₽\n')
