from asyncio import to_thread
from typing import Callable, Coroutine, Tuple, Dict, Any


def sync_to_async(function: Callable) -> Coroutine:

  async def wrapper(*args: Tuple, **kwargs: Dict) -> Any:
    return await to_thread(function, *args, **kwargs)

  return wrapper
