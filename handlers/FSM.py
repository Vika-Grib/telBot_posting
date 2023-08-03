from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from createBot import bot, dp
from aiogram.dispatcher.filters import Text
from keyboards import kb

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from createBot import chanal

ikb1 = InlineKeyboardButton(text='Опубликовать в канал', callback_data='da')
ikb2 = InlineKeyboardButton(text='Редактировать', callback_data='no')
inkb = InlineKeyboardMarkup(row_width=1).add(ikb1).add(ikb2)


class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    description = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    await FSMadmin.photo.set()
    await message.answer('Давай начнём!\nЗагрузи фото')
    await message.delete()


# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('OK, конструктор остановил работу')


imag = 1


@dp.message_handler(lambda message: not message.photo, state=FSMadmin.photo)
async def check_photo(message: types.Message, state: FSMContext):
    if message.text.lower() == 'без':
        async with state.proxy() as data:
            data['photo'] = None
        global imag
        imag = 2
        await FSMadmin.next()
        await message.answer('Тогда напиши заголовок')
    elif message.text == '/отмена':
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('OK, конструктор остановил работу')
    else:
        await message.answer('Пришли либо картинку, либо "без"')


# @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
# @dp.message_handler(lambda message: message.photo, state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMadmin.next()
    await message.reply(f'Теперь напиши заголовок')


# @dp.message_handler(content_types=['text'], state=FSMadmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if len(message.text) <= 70:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Теперь напиши описание')
    else:
        await message.answer('Слишком много символов. Думаю это не заголовок😝')


# @dp.message_handler(content_types=['text'], state=FSMadmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if imag == 2:
        if len(message.text) <= 4000:
            async with state.proxy() as data:
                data['description'] = message.text
            await bot.send_message(message.chat.id,
                                   f"<b><i><u>{data['name']}</u></i></b>\n"
                                   f"{data['description']}", parse_mode='html', reply_markup=inkb)
        else:
            await message.answer(f'Слишком много символов (на {len(message.text) - 4000} 😅)')
    else:
        if len(message.text) <= 950:
            async with state.proxy() as data:
                data['description'] = message.text
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=data['photo'],
                                 caption=f"<b><i><u>{data['name']}</u></i></b>\n"
                                         f"{data['description']}", parse_mode='html', reply_markup=inkb)
        else:
            await message.answer(f'Слишком много символов (на {len(message.text) - 1023} 😅)')
    global a
    a = data['photo']
    global b
    b = f"<b><i><u>{data['name']}</u></i></b>\n{data['description']}"
    global chat_id
    chat_id = message.chat.id
    await state.finish()


@dp.callback_query_handler(text='da')
async def da_call(callback: types.CallbackQuery):
    if imag == 2:
        await callback.bot.send_message(chanal, b, parse_mode='html')
    else:
        await callback.bot.send_photo(chat_id=chanal, photo=a, caption=b, parse_mode='html')
    await bot.send_message(chat_id, '<i>Сообщение в канале!</i>', parse_mode='html')


@dp.callback_query_handler(text='no')
async def net_call(callback: types.CallbackQuery):
    await callback.bot.send_message(chat_id, '<i>Начни конструктор объявления заново!</i>', parse_mode='html')


def register_hadnlers_FSM(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands=['отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_description, state=FSMadmin.description)
