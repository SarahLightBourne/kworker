from .telegram_bot import telegram_bot

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)
