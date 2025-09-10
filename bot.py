import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from database import init_db   

bot = Bot(token='8351177209:AAERJ5F15zT2dX3ZK1Fc4LMDrvEUi3E-kG4')
dp = Dispatcher()


async def main():
    init_db()  # <---- вызывайте функцию перед стартом бота
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())