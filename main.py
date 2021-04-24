"""
This is a echo bot.
It echoes any incoming text messages.
"""
import datetime
import logging

import yaml
from aiogram import Bot, Dispatcher, executor, types

from modules.calculations import (
    e_store,
    auction_ogz,
    contest_kgz,
    contest_ogz,
    auction_kgz,
)

CONFIG = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
API_TOKEN = CONFIG["api_token"]

WELCOME_MSG = """
Здравствуйте!
Я *КуЗя* (калькулятор закупок). Для расчета даты заключения контракта 
введите номер вида закупки из списка и планируемую дату передачи комплекта документов в ОГЗ.

*Список видов закупок*
1. Электронный магазин (НМЦК до 600 тыс. руб.)
2. Электронный аукцион через ОГЗ ( НМЦК до 3 млн. руб.)
3. Открытый конкурс в электронной форме через ОГЗ (НМЦК до 3 млн. руб.)
4. Электронный аукцион через КГЗ (НМЦК свыше 3 млн. руб.)
5. Открытый конкурс в электронной форме через КГЗ (НМЦК свыше 3 млн. руб.)

*Пример*
```
3 08.03.2021
```
"""

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

DP = Dispatcher(Bot(token=API_TOKEN))


def beautify_dict(data: dict[str, datetime.date]):
    return "\n".join(
        [f"*{k}*\n{v.day:02}.{v.month:02}.{v.year}\n" for (k, v) in data.items()]
    )


@DP.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(WELCOME_MSG, parse_mode="markdown")


@DP.message_handler()
async def echo(message: types.Message):
    user_input = message.text
    try:
        procedure_number_raw, start_date_raw = user_input.split(" ")
        procedure_number = int(procedure_number_raw)
        day, month, year = map(int, start_date_raw.split("."))
        start_date = datetime.date(year, month, day)
    except ValueError:
        if "ты" in user_input.lower():
            await message.answer(f"Нет {user_input.lower()} 😜")
        else:
            await message.answer("КуЗя Вас не понял 😥")
        raise
    if procedure_number == 1:
        result = e_store(start_date)
    elif procedure_number == 2:
        result = auction_ogz(start_date)
    elif procedure_number == 3:
        result = contest_ogz(start_date)
    elif procedure_number == 4:
        result = auction_kgz(start_date)
    elif procedure_number == 5:
        result = contest_kgz(start_date)
    else:
        result = None
        await message.answer("Выбрана несуществующая процедура!")
    await message.answer(beautify_dict(result), parse_mode="markdown")


if __name__ == "__main__":
    executor.start_polling(DP, skip_updates=True)
