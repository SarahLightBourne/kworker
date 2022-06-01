from ..settings.telegram_bot import telegram_bot
from ..settings.chosen_ones import CHOSEN_ONES

from re import Match
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup([[KeyboardButton('Favourites')]], resize_keyboard=True)


async def add(message: Message, regexp_command: Match) -> None:
  to_add = int(regexp_command.group(1))

  if to_add in CHOSEN_ONES.data:
    return await message.answer('This ID is already added')

  CHOSEN_ONES.add(to_add)
  await message.answer('Added')

  try:
    await telegram_bot.send_message(to_add, 'You have been added!', keyboard)
  except:
    pass
