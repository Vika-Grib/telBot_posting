from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from DataBase import Data_Base

class FSMadmin_description(StatesGroup):
    number = State()

# @dp.message_handler(commands=['статья'], state=None)
async def cm_start(message: types.Message):
    await FSMadmin_description.number.set()
    await message.answer('Напиши номер статьи')
    await message.delete()


# @dp.message_handler(content_types=['text'], state=FSMadmin_description.number)
async def load_description(message: types.Message, state: FSMContext):
    num_post = message
    await Data_Base.sql_number_img(num_post)
    await Data_Base.sql_number_name(num_post)
    await Data_Base.sql_number_description(num_post)
    await state.finish()


def register_hadnlers_FSM_description(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['статья'], state=None)
    dp.register_message_handler(load_description, state=FSMadmin_description.number)
