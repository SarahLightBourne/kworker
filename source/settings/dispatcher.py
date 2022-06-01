from .settings import CREATOR_ID
from .telegram_bot import telegram_bot

from ..handlers import (
  start_help,
  error,
  contact,
  sticker,
  add,
  remove,
  add_me,
  get_logs
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

dispatcher.register_message_handler(
  add,
  lambda msg: msg.from_user.id == CREATOR_ID,
  RegexpCommandsFilter([r'\/add ([0-9]+)'])
)

dispatcher.register_message_handler(
  remove,
  lambda msg: msg.from_user.id == CREATOR_ID,
  RegexpCommandsFilter([r'\/remove ([0-9]+)'])
)

dispatcher.register_message_handler(add_me, commands=['add_me'])

dispatcher.register_message_handler(
  get_logs,
  lambda msg: msg.from_user.id == CREATOR_ID,
  RegexpCommandsFilter([r'\/get_logs ([0-9]{4})_([0-9]{2})_([0-9]{2})'])
)
