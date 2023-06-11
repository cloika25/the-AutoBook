from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PLACEHOLDER_TEXT = "Выберите пункт меню"

AUTO_RU_CALLBACK = 'AUTO_RU_CALLBACK'

menu = [[InlineKeyboardButton(text="Auto.ru", callback_data=AUTO_RU_CALLBACK)]]

keyboard = InlineKeyboardMarkup(inline_keyboard=menu)