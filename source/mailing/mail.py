from ..kwork import kwork
from ..settings import telegram_bot
from ..settings.chosen_ones import CHOSEN_ONES

import asyncio

PROJECT_TEXT = '''<a href="{url}"><b>{title}</b> - <i>{category}</i></a>
{price}

{text}

Клиент: <b>{client_name}</b> - <code>{projects_count}</code> проектов
<b>{offers_count}</b>'''


async def mail() -> None:
  if not (projects := await kwork.get_new_projects()):
    return

  for project in projects[:1]:

    if (up_to := project['price']['price_up_to']):
      price = f'{project["price"]["price"]} - {up_to}'
    else:
      price = project['price']['price']

    project['price'] = f'<b>Цена:</b> <code>{price}</code>'

    text = PROJECT_TEXT.format(**project)

    for chosen_one in CHOSEN_ONES:
      await telegram_bot.send_message(chosen_one, text, parse_mode='HTML')

    await asyncio.sleep(1)
