from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.str("ADMINS")  # Тут у нас будет список из админов
IP = env.str("IP")  # Тоже str, но для айпи адреса хоста
PAYMENTS_PROVIDER_TOKEN = env.str("PAYMENTS_PROVIDER_TOKEN")  # Тестовая оплата Сбербанк

BD_USER = env.str('BD_USER')
BD_PASSWORD = env.str('BD_PASSWORD')
BD_NAME = env.str('BD_NAME')
HOST = env.str('HOST')
