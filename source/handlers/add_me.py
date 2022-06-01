from ..settings.settings import CREATOR_ID
from ..settings.chosen_ones import CHOSEN_ONES
from ..settings.telegram_bot import telegram_bot

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def add_me(message: Message, state: FSMContext) -> None:
  user_id = message.from_user.id

  if not user_id in CHOSEN_ONES.data:
    return await message.answer('You are already added')

  async with state.proxy() as data:

    if data.get('proposed') is True:
      return await message.answer('You have already asked to be added')
    
    data['proposed'] = True

  await telegram_bot.send_message(CREATOR_ID, f'Wants to be added <code>{user_id}</code> @{message.from_user.username}', parse_mode='HTML')
  await message.forward(CREATOR_ID)
