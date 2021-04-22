"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import yaml
from aiogram import Bot, Dispatcher, executor, types
from dateutil.parser import parse

from modules.keyboards import procedures_kb, procedure_btn_1, procedure_btn_2

CONFIG = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
API_TOKEN = CONFIG["api_token"]

welcome_msg = """
Здравствуйте, для запуска бота введите номер вида закупки из списка
и планируемую дату передачи комплекта документов в ОГЗ.

1. Электронный магазин (НМЦК до 600 тыс. руб.)
2. Электронный аукцион через ОГЗ ( НМЦК до 3 млн. руб.)
3. Открытый конкурс в электронной форме через ОГЗ (НМЦК до 3 млн. руб.)
4. Электронный аукцион через КГЗ (НМЦК свыше 3 млн. руб.)
5. Открытый конкурс в электронной форме через КГЗ (НМЦК свыше 3 млн. руб.)

Пример: *3 21.03.2021*"""

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
    await message.reply(welcome_msg, parse_mode='markdown')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    user_input = message.text
    procedure_number_raw, start_date_raw = user_input.split(" ")
    procedure_number = int(procedure_number_raw)
    start_date = parse(start_date_raw).date()
    if procedure_number == 1:
        result = do_some_func()
    elif procedure_number == 2:
        result = do_other_func()
    elif procedure_number == 3:
        result = do_other_func()
    elif procedure_number == 4:
        result = do_other_func()
    elif procedure_number == 5:
        result = do_other_func()

    await message.answer(result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
