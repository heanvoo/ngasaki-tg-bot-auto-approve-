import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import ChatJoinRequest, Message

API_TOKEN = '8958144806:AAE03meaypnYUy0GA7NIl_snAop0d6PiZ2w'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 1. Ответ на запуск бота (команда /start)
@dp.message(CommandStart())
async def start_handler(message: Message):
    logging.info(f"Получена команда /start от {message.from_user.id}")
    await message.answer(
        "Привет! Наш Telegram-канал:\n"
        "https://t.me/+R4gu7_qgwYswMjg6\n\n"
        "Переходи по ссылке и подавай заявку на вступление!"
    )

# 2. Обработка заявки на вступление
@dp.chat_join_request()
async def approve_request(req: ChatJoinRequest):
    user_id = req.from_user.id
    logging.info(f"Получена заявка от user_id: {user_id}")

    try:
        await bot.send_message(
            chat_id=user_id,
            text="Заявка принята, удачного использования Nagasaki Visuals!"
        )
        logging.info(f"УСПЕХ: Сообщение отправлено пользователю {user_id}")
    except Exception as e:
        logging.error(f"ОШИБКА ОТПРАВКИ ЛС ({user_id}): {type(e).__name__} — {e}")

    try:
        await req.approve()
        logging.info(f"Заявка от {user_id} успешно одобрена")
    except Exception as e:
        logging.error(f"Ошибка одобрения заявки: {e}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # Автоматически регистрируем все нужные типы событий (messages + chat_join_request)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
