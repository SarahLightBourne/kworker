from .settings import CREATOR_NICKNAME
from .telegram_bot import telegram_bot

from ..handlers import (
  start_help,
  error,
  contact,
  sticker,
  add,
  remove
)

from aiogram import Dispatcher
from aiogram.dispatcher.filters import RegexpCommandsFilter
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])
dispatcher.register_message_handler(error, commands=['error'])
dispatcher.register_message_handler(contact, commands=['contact'])
dispatcher.register_message_handler(sticker, content_types=['sticker'])

CREATOR_NICKNAME_LOWER = CREATOR_NICKNAME.lower()

dispatcher.register_message_handler(
  add,
  lambda msg: msg.from_user.username.lower() == CREATOR_NICKNAME_LOWER,
  RegexpCommandsFilter([r'/add ([0-9]+)'])
)

dispatcher.register_message_handler(
  remove,
  lambda msg: msg.from_user.username.lower() == CREATOR_NICKNAME_LOWER,
  RegexpCommandsFilter([r'/remove ([0-9]+)'])
)
