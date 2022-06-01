from ..settings.chosen_ones import CHOSEN_ONES

from re import Match
from aiogram.types import Message


async def remove(message: Message, regexp_command: Match) -> None:
  to_remove = int(regexp_command.group(1))

  if to_remove not in CHOSEN_ONES.data:
    return await message.answer("This ID isn't added")

  CHOSEN_ONES.remove(to_remove)
  await message.answer('Removed')
