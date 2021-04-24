from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

procedure_btn_1 = InlineKeyboardButton("1️⃣", callback_data="procedure_1")
procedure_btn_2 = InlineKeyboardButton("2️⃣", callback_data="procedure_2")
procedure_btn_3 = InlineKeyboardButton("3️⃣", callback_data="procedure_3")
procedure_btn_4 = InlineKeyboardButton("4️⃣", callback_data="procedure_4")
procedure_btn_5 = InlineKeyboardButton("5️⃣", callback_data="procedure_5")

procedures_kb = InlineKeyboardMarkup(row_width=5)
procedures_kb.add(
    procedure_btn_1,
    procedure_btn_2,
    procedure_btn_3,
    procedure_btn_4,
    procedure_btn_5,
)
