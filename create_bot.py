from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

# Что делать с токеном? он в .env
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
