import asyncio
from aiogram.utils.exceptions import NetworkError

from .mailing import background
from .utilities import requests_session
from .settings import authenticate, dispatcher, close_session


async def main() -> None:
  me = await authenticate()
  await requests_session.initialise()
  asyncio.create_task(background())

  print('Polling started as', me)
  await dispatcher.start_polling()


if __name__ == '__main__':

  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print('\nFinished')
  except NetworkError:
    print('Network Error')

  try:
    asyncio.run(close_session())
  except:
    pass
