from .category import Category
from ..settings import CATEGORIES

import orjson


class Kwork:

  def __init__(self):

    with open(CATEGORIES, 'rb') as file:
      categories = orjson.loads(file.read())

    self.categories = [
      Category(category['name'], category['params'])
    for category in categories]
