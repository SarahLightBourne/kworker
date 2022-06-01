import asyncio
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext


async def favourite(callback_query: CallbackQuery, state: FSMContext):
  async with state.proxy() as data:
    data.setdefault('favourites', []).append(callback_query.message.message_id)

  await asyncio.gather(
    callback_query.answer('Added to favourites 🟢'),
    callback_query.message.edit_reply_markup()
  )
