import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

API_TOKEN = '8638681791:AAGH2Ll2URmCY7te-KZZleQ0J8WeTieQ9y4'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_request(req: ChatJoinRequest):
    await req.approve()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
