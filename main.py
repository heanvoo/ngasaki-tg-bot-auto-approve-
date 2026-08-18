import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

API_TOKEN = '8958144806:AAE03meaypnYUy0GA7NIl_snAop0d6PiZ2w'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_request(req: ChatJoinRequest):
    user_id = req.from_user.id
    logging.info(f"Получена заявка от user_id: {user_id}")

    # 1. Пытаемся отправить сообщение в ЛС
    try:
        await bot.send_message(
            chat_id=user_id,
            text="Заявка принята, удачного использования Ngasaki Visuals!"
        )
        logging.info(f"УСПЕХ: Сообщение отправлено пользователю {user_id}")
    except Exception as e:
        logging.error(f"ОШИБКА ОТПРАВКИ ЛС ({user_id}): {type(e).__name__} — {e}")

    # 2. Одобряем заявку в канал
    try:
        await req.approve()
        logging.info(f"Заявка от {user_id} успешно одобрена")
    except Exception as e:
        logging.error(f"Ошибка одобрения заявки: {e}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=["chat_join_request"])

if __name__ == '__main__':
    asyncio.run(main())
