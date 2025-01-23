#Методы отправки сообщений
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


api = None
with open('bot_api.txt', 'r', encoding='utf-8') as file:
    for line in file:
        api = str(line)


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.reply("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply("Введите команду /start, чтобы начать общение.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)