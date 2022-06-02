from httpx import AsyncClient
from fake_headers import Headers
from subprocess import Popen, PIPE

import signal, os
from sys import exit
from .sync_to_async import sync_to_async
from ..settings import TOR_PROCESS, TOR_PORT


class RequestsSession:
  CHECK_URL = 'https://kwork.ru/projects'

  def __init__(self) -> None:
    self.process_id = None
    self.requests_session: AsyncClient = None

  async def initialise(self) -> None:
    status = await self.run_tor()

    if status == 'new':
      await self.refresh()

  async def refresh(self) -> None:
    while not await self.check():
      os.kill(self.process_id, signal.SIGKILL)
      await self.run_tor()

  async def check(self) -> bool:
    session = await self.get_requests_session()
    response = await session.get(self.CHECK_URL)

    if response.status_code == 200:
      return True

    return False

  @sync_to_async
  def run_tor(self) -> str:

    process = Popen(
      f'tor --SOCKSPort {TOR_PORT} --ControlPort {TOR_PORT + 1}',
      shell=True,
      stdout=PIPE
    )

    for line in process.stdout:
      line = str(line)

      if 'Bootstrapped 100%' in line:
        self.process_id = process.pid
        self.write_process()
        return 'new'
      elif 'Address already in use' in line:
        self.read_process()
        return 'old'

  def write_process(self) -> None:
    with open(TOR_PROCESS, 'w') as file:
      print(self.process_id, file=file)

  def read_process(self) -> None:
    try:
      with open(TOR_PROCESS, 'r') as file:
        self.process_id = int(file.read())
    except Exception as error:
      print(error)
      exit(1)

  async def get_requests_session(self) -> AsyncClient:
    return self.requests_session or AsyncClient(headers=Headers().generate(), timeout=1000, proxies=f'socks5://127.0.0.1:{TOR_PORT}')

  async def close_requests_session(self) -> None:
    if self.requests_session:
      await self.requests_session.aclose()
