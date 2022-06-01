from aiogram.types import Message


async def sticker(message: Message):
  print(message.sticker.file_id)
  await message.answer_sticker(message.sticker.file_id)
