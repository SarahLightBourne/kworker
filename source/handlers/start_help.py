from aiogram.types import Message

response_text = '''This bot will send notifications only for the chosen ones'''


async def start_help(message: Message) -> None:
  await message.answer(response_text)
