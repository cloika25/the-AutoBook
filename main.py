
from aiogram.utils import executor
from aiogram import types
from create_bot import dp, bot
import consts
from keyboards.menu_keyboard import keyboard as menuKeyboard, PLACEHOLDER_TEXT as menuPlaceholderText, AUTO_RU_CALLBACK


async def on_startup(_):
    print('PROJECT LAUNCHED')


@dp.message_handler(commands=['start'])
async def hello_message(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, consts.HELLO_MESSAGE)
    except Exception as error:
        print(str(error))


@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, menuPlaceholderText, reply_markup=menuKeyboard)
    except Exception as error:
        print(str(error))


@dp.callback_query_handler(text=AUTO_RU_CALLBACK)
async def parse_auto_ru(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'колбэк на авто ру')
    except Exception as error:
        print(str(error))


@dp.message_handler()
async def echo_send(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, message.text)
    except Exception as error:
        print(str(error))


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
