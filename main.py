
from aiogram.utils import executor
from aiogram import types
from create_bot import dp, bot


async def on_startup(_):
    print('PROJECT LAUNCHED')


@dp.message_handler()
async def echo_send(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, message.text)
    except Exception as error:
        print(str(error))


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
