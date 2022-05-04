from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.str("ADMINS")
IP = env.str("IP")
PAYMENTS_PROVIDER_TOKEN = env.str("PAYMENTS_PROVIDER_TOKEN")

BD_USER = env.str('BD_USER')
BD_PASSWORD = env.str('BD_PASSWORD')
BD_NAME = env.str('BD_NAME')
HOST = env.str('HOST')
