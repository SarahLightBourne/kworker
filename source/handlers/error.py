from aiogram.types import Message

response_text = '''Error has been reported'''


async def error(message: Message) -> None:
  await message.answer(response_text)
