import orjson
from .settings import CHOSEN_ONES

with open(CHOSEN_ONES, 'rb') as file:
  CHOSEN_ONES = orjson.loads(file.read())
