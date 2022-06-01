from ..settings.settings import CREATOR_ID
from ..settings.chosen_ones import CHOSEN_ONES
from ..settings.telegram_bot import telegram_bot

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
    await telegram_bot.send_message(CREATOR_ID, f'Error reported by {message.from_user.id}')
    await message.forward(CREATOR_ID)
