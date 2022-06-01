from aiogram.types import Message
from ..settings import CREATOR_NICKNAME


async def contact(message: Message) -> None:
  print(message.from_user.id)
  await message.answer(f'@{CREATOR_NICKNAME}')
