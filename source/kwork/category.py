from ..utilities import requests_session, log_error

import asyncio
from re import compile
from bs4 import BeautifulSoup
from httpx import AsyncClient
from typing import Dict, List, Union

name_re = compile(r'ь\: ([^\n]+)')
projects_re = compile(r'(\d+)')


class Category:
  URL = 'https://kwork.ru/projects?view=0'
  PROJECT_URL = 'https://kwork.ru/projects/{project_id}/view'

  def __init__(self, name: str, params: Dict) -> None:
    self.name, self.params = name, params
    self.projects_cache: List[str] = list()

  def update_cache(self, item: int, limit: int = 100) -> None:
    self.projects_cache.insert(0, item)
    self.projects_cache = self.projects_cache[:limit]

  async def parse_category(self, session: AsyncClient) -> Union[List[Dict], str, None]:
    try:

      for counter in range(5):
        if ((response := await session.get(self.URL, params=self.params)).status_code != 200):
          await asyncio.sleep(1 * counter)
          continue
        else:
          break

      else:
        log_error("Can't get response")
        return 'error'

      return self.__parse(response.text)
    except Exception as error:
      log_error(error)
      raise ConnectionError

  def __parse(self, html_code: str) -> Union[List[Dict], None]:
    result: List[Dict] = list()
    parser = BeautifulSoup(html_code, 'html.parser')

    for project in parser.find_all(class_='card'):

      if (project_id := int(project.get('data-id'))) in self.projects_cache:
        continue

      self.update_cache(project_id)
      title = project.find('a').text.strip()
      text = project.find(class_='wants-card__description-text').text.split('Показать полностью')[1].rstrip('Скрыть').strip()

      if (avatar := project.find(class_='user-avatar__picture') or None):
        if not (avatar := avatar.get('data-srcset')):
          avatar = None
        else:
          avatar = list(map(str.strip, avatar.split(',')))[-1].split(' ')[0].strip()

      statistics = project.find(class_='want-payer-statistic').text
      client_name = name_re.findall(statistics)[0].strip()
      projects_count = projects_re.findall(statistics)[0].strip()

      step = project.find(class_='query-item__info').text.split(' \xa0\xa0\xa0')
      if len(step) == 1:
        time_left = None
        offers_count = step[0].strip()
      else:
        time_left, offers_count = step
        time_left, offers_count = time_left.strip(), offers_count.strip()

      price_string = project.find(class_='wants-card__right').text

      if 'Цена до:' in price_string:
        price = {'price': price_string.split('до: ')[1].replace(' ', '.').replace('\xa0', ''), 'price_up_to': None}
      elif 'Желаемый бюджет' in price_string:
        price_string = price_string.split(': до ')
        price = {'price': price_string[1].replace(' ', '.').replace('\xa0', '').replace('Допустимый', ''), 'price_up_to': price_string[2].replace(' ', '.').replace('\xa0', '')}
      else:
        price = {'price': price_string.replace('Цена ', '').replace('\xa0', '')}

      result.append({
        'id': project_id,
        'title': title,
        'text': text,
        'client_name': client_name,
        'projects_count': projects_count,
        'time_left': time_left,
        'offers_count': offers_count,
        'price': price,
        'avatar': avatar,
        'url': self.PROJECT_URL.format(project_id=project_id),
        'category': self.name
      })

    return result or None
