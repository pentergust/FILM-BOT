"""Общие настройкм бота.

Некоторые параметры читает из переменных окржения (.env) файла.
"""

from os import getenv

from dotenv import load_dotenv

# Подгружаем .env файлик
load_dotenv()

# Токен от Telegram Бота
BOT_TOKEN = getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    raise RuntimeError("You must specify telegram bot token in env")

# Токен от Kinopoisk
# Используется чтобы получать тайтлы
# Получить токен: https://kinopoisk.dev/
KINOPOISK_TOKEN = getenv("KINOPOISK_TOKEN")

if KINOPOISK_TOKEN is None:
    raise RuntimeError("You must specify kinipoisk token in env")
