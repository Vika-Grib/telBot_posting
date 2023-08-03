from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from DataBase import Data_Base
from createBot import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


del_ikb1 = InlineKeyboardButton(text='Удалить', callback_data='yes')
del_ikb2 = InlineKeyboardButton(text='Нет', callback_data='net')
del_inkb = InlineKeyboardMarkup(row_width=2).add(del_ikb1).add(del_ikb2)

class FSMadmin_delete_post(StatesGroup):
    number = State()


# @dp.message_handler(commands=['удалить_пост'], state=None)
async def cm_start(message: types.Message):
    await FSMadmin_delete_post.number.set()
    await message.answer('Напиши номер статьи для удаления')
    await message.delete()


# @dp.message_handler(content_types=['text'], state=FSMadmin_description.number)
async def load_description(message: types.Message, state: FSMContext):
    global num_post
    num_post = message
    await Data_Base.sql_number_name(num_post)
    await bot.send_message(message.from_user.id, 'Заголовок этой статьи?', reply_markup=del_inkb)
    await state.finish()
    global chat_id
    chat_id = message.from_user.id


@dp.callback_query_handler(text='yes')
async def yes_call(callback: types.CallbackQuery):
    await Data_Base.sql_post_delete(num_post)
    await callback.bot.send_message(chat_id, '<i>Статья удалена!</i>', parse_mode='html')


@dp.callback_query_handler(text='net')
async def net_call(callback: types.CallbackQuery):
    await callback.bot.send_message(chat_id, '<i>Ничего не удалено!</i>', parse_mode='html')


def register_hadnlers_FSM_delete_post(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['удалить_пост'], state=None)
    dp.register_message_handler(load_description, state=FSMadmin_delete_post.number)
