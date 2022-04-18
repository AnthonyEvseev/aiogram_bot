import sqlite3 as sq


async def sql_create_db():
    global base, cur
    base = sq.connect('store_data.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    # SQL запрос на создание таблицы 'store_menu'
    base.execute('CREATE TABLE IF NOT EXISTS store_menu(item_id INTEGER PRIMARY KEY,name TEXT, '
                 'discription TEXT, price INTEGER, img_item TEXT)')

    # SQL запрос на создание таблицы 'shopping_cart'
    base.execute('CREATE TABLE IF NOT EXISTS user_id(user_id INTEGER PRIMARY KEY,'
                 'order_id INTEGER)')

    base.execute('CREATE TABLE IF NOT EXISTS order_id(order_id INTEGER PRIMARY KEY,'
                 'item_id INTEGER, amount_item INTEGER, FOREIGN KEY (order_id) REFERENCES order_id (user_id))')

    # base.execute('CREATE TABLE IF NOT EXISTS shopping_cart(order_id INTEGER PRIMARY KEY, user_id INTEGER, '
    #              'item_id INTEGER, amount_item INTEGER, FOREIGN KEY (item_id) REFERENCES item_id (store_menu))')

    # SQL запрос на создание таблицы 'order_history'
    # base.execute('CREATE TABLE IF NOT EXISTS order_history(order_id INTEGER PRIMARY KEY, user_id INTEGER, '
    #              'item_id INTEGER, amount_item INTEGER, FOREIGN KEY (item_id) REFERENCES item_id (store_menu))')
    base.commit()


# Записывает в БД товары введенное админом в чате
async def sql_append_item_store_menu(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO store_menu VALUES ( NULL, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# Запрашиваю данные из БД.
async def sql_read_store_menu():
    return cur.execute('SELECT * FROM store_menu').fetchall()


async def sql_cart_add(current_amount):
    pass
    # async with state.proxy() as data:
    #     cur.execute('INSERT INTO store_menu VALUES ( NULL, ?, ?, ?, ?)', tuple(data.values()))
    #     base.commit()


# Запрос на удалиение
async def sql_delete_item_store_menu(data):
    return cur.execute('DELETE FROM store_menu WHERE name == ?', (data,)), base.commit()
