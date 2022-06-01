from ..settings.chosen_ones import CHOSEN_ONES

import asyncio
from aiogram.types import Message

response_text = '''Error has been reported'''


async def error(message: Message) -> None:

  if message.from_user.id not in CHOSEN_ONES.data:
    await message.answer("You're not the chosen one, you can't report anything")
    await asyncio.sleep(1)
    await message.answer_sticker('CAACAgUAAxkBAAMmYpbwUvyU_bxZ6yWeOIWDUpIjf3MAApEGAAKcnShWpDQwb4hZSEEkBA')
  else:
    await message.answer(response_text)
    print('Error reported by', message.from_user.username, message.from_user.id)
