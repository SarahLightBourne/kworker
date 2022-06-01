from .mail import mail

import asyncio
import aioschedule


async def background() -> None:
  aioschedule.every().minute.do(mail)
  await aioschedule.run_all()

  while True:
    await asyncio.sleep(1)
    await aioschedule.run_pending()
