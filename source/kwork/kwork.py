from .category import Category
from ..settings import CATEGORIES
from ..utilities import requests_session

import asyncio, orjson
from functools import reduce
from typing import List, Dict, Union


class Kwork:
  first_run = True

  def __init__(self):

    with open(CATEGORIES, 'rb') as file:
      categories = orjson.loads(file.read())

    self.categories = [
      Category(category['name'], category['params'])
    for category in categories]

  async def get_new_projects(self) -> Union[List[Dict], None]:
    results = list()

    for category in self.categories:
      session = await requests_session.get_requests_session()

      while True:
        try:
          result = await category.parse_category(session)
        except ConnectionError:
          await requests_session.refresh()
          continue
        else:
          results.append(result)
          break

      await asyncio.sleep(1)

    # if self.first_run:
    #   self.first_run = False
    #   return None

    if (results := list(filter(lambda el: el, results))):
      return list(reduce(lambda a, x: a + x, results))

    return None
