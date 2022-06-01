from ..utilities import requests_session

from re import compile
from bs4 import BeautifulSoup
from typing import Dict, List, Union

name_re = compile(r'ь\: ([^\n]+)')
projects_re = compile(r'(\d+)')


class Category:
  URL = 'https://kwork.ru/projects'
  PROJECT_URL = 'https://kwork.ru/projects/{project_id}/view'

  def __init__(self, name: str, params: Dict) -> None:
    self.name, self.params = name, params
    self.projects_cache: List[str] = list()

  def update_cache(self, item: int, limit: int = 15) -> None:
    print(item)
    self.projects_cache.insert(0, item)
    self.projects_cache = self.projects_cache[:limit]

  async def parse_category(self) -> Union[List[Dict], None]:
    session = await requests_session.get_requests_session()

    if ((response := await session.get(self.URL, params=self.params)).status_code != 200):
      return print("Can't get response")

    result: List[Dict] = list()
    parser = BeautifulSoup(response.text, 'html.parser')

    for project in parser.find_all(class_='card'):

      if (project_id := project.get('data-id')) in self.projects_cache:
        continue

      self.update_cache(project_id)
      title = project.find('a').text.strip()
      text = project.find(class_='wants-card__description-text').text.split('Показать полностью')[1].rstrip('Скрыть').strip()

      if (avatar := project.find(class_='user-avatar__picture') or None):
        avatar = list(map(str.strip, avatar.get('data-srcset').split(',')))[-1]

      statistics = project.find(class_='want-payer-statistic').text
      client_name = name_re.findall(statistics)[0].strip()
      projects_count = projects_re.findall(statistics)[0].strip()
      time_left, offers_count = project.find(class_='query-item__info').text.split(' \xa0\xa0\xa0')
      time_left, offers_count = time_left.strip(), offers_count.strip()
      price_string = project.find(class_='wants-card__right').text

      if 'до:' in price_string:
        price = {'price': price_string.split('до: ')[1].replace(' ', '.').replace('\xa0', ''), 'price_up_to': None}
      else:
        price_string = price_string.split(': до ')
        price = {'price': price_string[1].replace(' ', '.').replace('\xa0', '').replace('Допустимый', ''), 'price_up_to': price_string[2].replace(' ', '.').replace('\xa0', '')}

      result.append({
        'title': title,
        'text': text,
        'client_name': client_name,
        'projecgts_count': projects_count,
        'time_left': time_left,
        'offers_count': offers_count,
        'price': price,
        'url': self.PROJECT_URL.format(project_id=project_id)
      })

    return result
