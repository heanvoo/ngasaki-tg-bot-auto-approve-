import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

API_TOKEN = '8958144806:AAE03meaypnYUy0GA7NIl_snAop0d6PiZ2w'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_request(req: ChatJoinRequest):
    # 1. Принимаем заявку
    await req.approve()
    logging.info(f"Заявка от {req.from_user.id} принята")

    # Небольшая пауза перед отправкой ЛС
    await asyncio.sleep(0.5)

    # 2. Отправляем сообщение
    try:
        await bot.send_message(
            chat_id=req.from_user.id,
            text="Заявка принята, удачного использования Ngasaki Visuals!"
        )
        logging.info(f"Сообщение успешно отправлено {req.from_user.id}")
    except Exception as e:
        logging.error(f"Не удалось отправить сообщение {req.from_user.id}: {e}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
