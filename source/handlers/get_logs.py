from ..settings.settings import LOG, CREATOR_ID
from ..settings.telegram_bot import telegram_bot

import os
from re import Match
from aiogram.types import Message


async def get_logs(message: Message, regexp_command: Match) -> None:
  filepath = LOG / ('_'.join(map(str, regexp_command.groups())) + '.log')

  if not os.path.exists(filepath):
    return await message.answer(f'{filepath} does not exist')

  with open(filepath, 'r') as file:
    await telegram_bot.send_document(CREATOR_ID, file)
