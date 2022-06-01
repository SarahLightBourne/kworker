from ..settings.chosen_ones import CHOSEN_ONES

import asyncio
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

response_text = '''This bot will send notifications only for the chosen ones'''
keyboard = ReplyKeyboardMarkup([[KeyboardButton('Favourites')]], resize_keyboard=True)


async def start_help(message: Message) -> None:
  await message.answer(response_text, reply_markup=keyboard)

  if message.from_user.id not in CHOSEN_ONES.data:
    await asyncio.sleep(1.5)
    await message.answer('And you are not one of them', reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(0.5)
    await message.answer_sticker('CAACAgUAAxkBAAMgYpbv61oOZ1jE7Px9nao7Tc1-5cgAAnEFAAKJtghU0hVICaDlFJ8kBA')
