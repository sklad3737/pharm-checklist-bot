import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import BOT_TOKEN

bot = Bot(token=8685523885AAHrCdbbi67sidWIhJ94ji5oyGrfgXba284)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Бот Фарм-Контроль запущен.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())

