from .mail import mail

import asyncio
import aioschedule


async def background() -> None:
  aioschedule.every(5).minutes.do(mail)
  await aioschedule.run_all()

  while True:
    await asyncio.sleep(1)
    await aioschedule.run_pending()
