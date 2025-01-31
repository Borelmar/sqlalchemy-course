import asyncio
from bot import start_bot
import database

if __name__ == '__main__':
    database.create_schema()
    asyncio.run(start_bot())