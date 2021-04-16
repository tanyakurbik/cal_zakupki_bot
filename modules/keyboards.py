from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

procedure_msg_1 = "1. Электронный магазин (НМЦК до 600 тыс. руб.)"
procedure_msg_2 = "2. Электронный аукцион через ОГЗ ( НМЦК до 3 млн. руб.)"
procedure_msg_3 = "3. Открытый конкурс в электронной форме через ОГЗ (НМЦК до 3 млн. руб.)"
procedure_msg_4 = "4. Электронный аукцион через КГЗ (НМЦК свыше 3 млн. руб.)"
procedure_msg_5 = "5. Открытый конкурс в электронной форме через КГЗ (НМЦК свыше 3 млн. руб.)"

procedure_btn_1 = InlineKeyboardButton(procedure_msg_1, callback_data="procedure_1")
procedure_btn_2 = InlineKeyboardButton(procedure_msg_2, callback_data="procedure_2")
procedure_btn_3 = InlineKeyboardButton(procedure_msg_3, callback_data="procedure_3")
procedure_btn_4 = InlineKeyboardButton(procedure_msg_4, callback_data="procedure_4")
procedure_btn_5 = InlineKeyboardButton(procedure_msg_5, callback_data="procedure_5")

procedures_kb = InlineKeyboardMarkup()
procedures_kb.add(procedure_btn_1)
procedures_kb.add(procedure_btn_2)
procedures_kb.add(procedure_btn_3)
procedures_kb.add(procedure_btn_4)
procedures_kb.add(procedure_btn_5)
