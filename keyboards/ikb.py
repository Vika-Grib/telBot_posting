from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


urlkb = InlineKeyboardMarkup(row_width=1)
ukb1 = InlineKeyboardButton(text='Открыть таблицу', url='https://docs.google.com/spreadsheets/d/1u03Mr9HDlcTBjy0lybpgMUVNBzEep0G7HwLjOxEdZas/edit#gid=0')
urlkb.add(ukb1)

