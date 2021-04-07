from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

procedure_btn_1 = InlineKeyboardButton('Снятие мишек с деревьев',
                                       callback_data='get_bear_from_tree')
procedure_btn_2 = InlineKeyboardButton('Рассчитать стоимость пупусек', callback_data='calc_price')

procedures_kb = InlineKeyboardMarkup().add(procedure_btn_1)
procedures_kb.add(procedure_btn_2)
