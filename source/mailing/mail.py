from ..kwork import kwork
from ..settings import telegram_bot
from ..settings.chosen_ones import CHOSEN_ONES
from ..utilities import requests_session, log_error

from aiogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup
)

import asyncio
from io import BytesIO

PROJECT_TEXT = '''<a href="{url}"><b>{title}</b> - <i>{category}</i></a>
{price}

{text}

Клиент: <b>{client_name}</b> - <code>{projects_count}</code> проектов
<b>{offers_count}</b>'''


async def mail() -> None:
  if not (projects := await kwork.get_new_projects()):
    return

  session = await requests_session.get_requests_session()

  for project in projects:

    if (up_to := project['price'].get('price_up_to')):
      price = f'{project["price"]["price"]} - {up_to}'
    else:
      price = project['price']['price']

    project['price'] = f'<b>Цена:</b> <code>{price}</code>'
    time_left = project.pop('time_left')

    text = PROJECT_TEXT.format(**project)

    if time_left:
      text += f'\n\n<i>{time_left}</i>'

    if project['avatar']:
      response = await session.get(project['avatar'])
      avatar = True
    else:
      avatar = False

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('To favourites', callback_data=f'favourite_{project["id"]}')]])

    for chosen_one in CHOSEN_ONES.data:

      try:
        if avatar:
          await telegram_bot.send_photo(chosen_one, BytesIO(response.read()), caption=text, parse_mode='HTML', reply_markup=keyboard)
        else:
          await telegram_bot.send_message(chosen_one, text, parse_mode='HTML', disable_web_page_preview=True, reply_markup=keyboard)
      except Exception as error:
        log_error(error)

      await asyncio.sleep(0.5)

    await asyncio.sleep(1)
