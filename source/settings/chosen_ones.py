import orjson
from .settings import CHOSEN_ONES as PATH


class ChosenOnes:

  def __init__(self) -> None:
    self.data, self.index = list(), 0
    self.read()

  def read(self) -> None:
    with open(PATH, 'rb') as file:
      self.data = orjson.loads(file.read())

  def write(self, item: int) -> None:
    self.data.append(item)

    with open(PATH, 'wb') as file:
      file.write(orjson.dumps(self.data, option=orjson.OPT_INDENT_2))


CHOSEN_ONES = ChosenOnes()
