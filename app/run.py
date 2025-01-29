import asyncio
#from bot import start_bot
from database import init_db, test

async def main():
    #await start_bot()
    await test()

if __name__ == '__main__':
    init_db()
    asyncio.run(main())