import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN
from database import engine, Base
from states import RegisterState
from models import User

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())


# ----------------------------
# Создание таблиц БД
# ----------------------------

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# ----------------------------
# /start
# ----------------------------

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Бот Фарм-Контроль запущен.\n"
        "Для регистрации отправьте /register"
    )


# ----------------------------
# Начало регистрации
# ----------------------------

@dp.message(F.text == "/register")
async def register_start(message: Message, state: FSMContext):
    await state.set_state(RegisterState.fio)

    await message.answer("Введите ваше ФИО:")


# ----------------------------
# Обработка FSM регистрации
# ----------------------------

@dp.message(RegisterState.fio)
async def process_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)

    await state.set_state(RegisterState.pharmacy)

    await message.answer("Введите название аптеки:")


# ----------------------------
# Запуск бота
# ----------------------------

async def main():
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
