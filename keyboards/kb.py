from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/загрузить')
b3 = KeyboardButton('/отмена')
b4 = KeyboardButton('/список')
b5 = KeyboardButton('/статья')
b6 = KeyboardButton('/удалить_пост')
b7 = KeyboardButton('/start')
b10 = KeyboardButton('/таблица')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_post = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_main.add(b1).add(b4).add(b10)
kb_post.add(b4).add(b2, b3).add(b5, b6).add(b7)
