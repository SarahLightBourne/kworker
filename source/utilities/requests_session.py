from httpx import AsyncClient


class RequestsSession:

  def __init__(self) -> None:
    self.requests_session: AsyncClient = None

  async def get_requests_session(self) -> AsyncClient:
    return self.requests_session or AsyncClient(timeout=1000)

  async def close_requests_session(self) -> None:
    if self.requests_session:
      await self.requests_session.aclose()
