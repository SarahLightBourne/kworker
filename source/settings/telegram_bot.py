from sys import exit
from .settings import TG_TOKEN

from aiogram import Bot
from aiogram.utils.exceptions import ValidationError, Unauthorized

try:
  telegram_bot = Bot(TG_TOKEN)
except ValidationError:
  print('Telegram Token is invalid')
  exit(1)


async def close_session() -> None:
  await (await telegram_bot.get_session()).close()


async def authenticate() -> str:

  try:
    me = await telegram_bot.get_me()
  except Unauthorized:
    print('Token is unauthorized')
    await close_session()
    exit(1)

  return me.first_name
