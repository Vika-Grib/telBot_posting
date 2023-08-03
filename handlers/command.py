from aiogram import types, Dispatcher
from createBot import dp, bot
from DataBase import Data_Base
from keyboards import kb_main, kb_post, urlkb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот!', reply_markup=kb_main)
    await message.delete()


# @dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'<b>Таблица</b> - список объявлений(google)\n'
                                                 f'<b><i>Выгрузка объявления:</i></b>\n'
                                                 f'<b>Загрузить</b> - пошаговое создание поста\n'
                                                 f'<b>Отмена</b> - выход из процесса создания поста\n'
                                                 f'<b><i>Работа со статьями:</i></b>\n'
                                                 f'<b>Список</b> - список название статей\n'
                                                 f'<b>Статья</b> - просмотр статьи по номер\n'
                                                 f'<b>Удалить пост</b> - удалить пост по номеру', parse_mode='html')
    await message.delete()


# @dp.message_handler(commands=['таблица'])
async def table(message: types.Message):
    await bot.send_message(message.from_user.id, '👁 Таблица объявлений ✍️', reply_markup=urlkb)
    await message.delete()


ikb_list1 = InlineKeyboardButton(text='еще 10 ->', callback_data='list1')
ikb_list = InlineKeyboardMarkup(row_width=1).add(ikb_list1)
ikb_list2 = InlineKeyboardButton(text='еще 1 ->', callback_data='list2')
ikb2_list = InlineKeyboardMarkup(row_width=1).add(ikb_list2)


# @dp.message_handler(commands=['список'])
async def read_db(message: types.Message):
    await Data_Base.sql_read(message)
    await bot.send_message(message.from_user.id, '-' * 10, reply_markup=kb_post)
    await bot.send_message(message.from_user.id, 'Далее?', reply_markup=ikb_list)
    global chat_id
    chat_id = message.from_user.id


@dp.callback_query_handler(text='list1')
async def yes_call(callback: types.CallbackQuery):
    await Data_Base.sql_read2(callback)
    await callback.bot.send_message(chat_id, 'Далее?', reply_markup=ikb2_list)


@dp.callback_query_handler(text='list2')
async def yes_call(callback: types.CallbackQuery):
    await Data_Base.sql_read3(callback)
    await callback.bot.send_message(chat_id, 'пока так)')


def register_hadnlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(table, commands=['таблица'])
    dp.register_message_handler(read_db, commands=['список'])
