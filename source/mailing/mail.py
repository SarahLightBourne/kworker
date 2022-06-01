from ..kwork import kwork
from ..settings import telegram_bot
from ..utilities import requests_session
from ..settings.chosen_ones import CHOSEN_ONES

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

    if (up_to := project['price']['price_up_to']):
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
      avatar = BytesIO(response.read())

    for chosen_one in CHOSEN_ONES:
      await telegram_bot.send_photo(chosen_one, avatar, caption=text, parse_mode='HTML')
      await asyncio.sleep(0.5)

    await asyncio.sleep(1)
