from .telegram_bot import telegram_bot

from ..handlers import (
  start_help,
  error,
  contact,
  sticker
)

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])
dispatcher.register_message_handler(error, commands=['error'])
dispatcher.register_message_handler(contact, commands=['contact'])
dispatcher.register_message_handler(sticker, content_types=['sticker'])
