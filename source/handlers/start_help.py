from ..settings.chosen_ones import CHOSEN_ONES

import asyncio
from aiogram.types import Message

response_text = '''This bot will send notifications only for the chosen ones'''


async def start_help(message: Message) -> None:
  await message.answer(response_text)

  if message.from_user.id not in CHOSEN_ONES:
    await asyncio.sleep(1.5)
    await message.answer('And you are not one of them')
    await asyncio.sleep(0.5)
    await message.answer_sticker('CAACAgUAAxkBAAMgYpbv61oOZ1jE7Px9nao7Tc1-5cgAAnEFAAKJtghU0hVICaDlFJ8kBA')
