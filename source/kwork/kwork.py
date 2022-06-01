from .category import Category
from ..settings import CATEGORIES

import asyncio, orjson
from functools import reduce
from typing import List, Dict, Union


class Kwork:

  def __init__(self):

    with open(CATEGORIES, 'rb') as file:
      categories = orjson.loads(file.read())

    self.categories = [
      Category(category['name'], category['params'])
    for category in categories]

  async def get_new_projects(self) -> Union[List[Dict], None]:

    results = await asyncio.gather(*[
      category.parse_category()
    for category in self.categories])

    if (results := list(filter(lambda el: el, results))):
      return list(reduce(lambda a, x: a + x, results))

    return None
