from ..settings import LOG

import os
from typing import Union
from datetime import datetime


def log_error(error: Union[Exception, str]) -> None:

  if not os.path.exists(LOG):
    os.mkdir(LOG)

  path = LOG / f'{datetime.now().strftime("%Y_%m_%d")}.log'

  message = f'{type(error)} {str(error)}' if type(error) is Exception else error

  with open(path, 'a') as file:
    print('ERROR', message, file=file)
