"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import yaml
from aiogram import Bot, Dispatcher, executor, types

from modules.keyboards import procedures_kb, procedure_btn_1, procedure_btn_2

CONFIG = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
API_TOKEN = CONFIG["api_token"]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Здравствуйте, какой вид процедуры вы планируете провести?",
                        reply_markup=procedures_kb)


@dp.callback_query_handler(lambda call: call.data == procedure_btn_1.callback_data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        'Пока вы снимали мишку, вам на голову упал блин! \nДелю случайное число на ноль!'
    )


@dp.callback_query_handler(lambda call: call.data == procedure_btn_2.callback_data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        'Стоимость одного килограма дружков-крендельков составляет два '
        'пирожка украшенных ста граммами глаз королевских креветок!'
    )



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
