from ..settings.telegram_bot import telegram_bot

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def list_favourites(message: Message, state: FSMContext):
  user_id = message.from_user.id

  async with state.proxy() as data:
    if not (favourites := data.get('favourites')):
      return await message.answer('You have no favourites')

    for message_id in favourites:
      await telegram_bot.forward_message(user_id, user_id, message_id)

    del data['favourites']
