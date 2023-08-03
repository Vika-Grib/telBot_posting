from aiogram import types, Dispatcher
from createBot import dp, bot


# @dp.message_handler()
async def len_send(message: types.Message):
    await bot.send_message(message.from_user.id, f"{len(message.text)} символов. \n(С картинкой - 950(1024), без 4000(4092))")



def register_hadnlers_other(dp: Dispatcher):
    dp.register_message_handler(len_send)