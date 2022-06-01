from aiogram.types import Message
from ..settings import CREATOR_NICKNAME


async def contact(message: Message) -> None:
  await message.answer(f'@{CREATOR_NICKNAME}')
