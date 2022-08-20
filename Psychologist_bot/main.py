
import config

from aiogram import Bot, Dispatcher, executor, types

from classes.person_manager import Person_manager as Pm

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """Реагирование на команду старт."""
    print(message.from_user.id)
    await Pm().new_person(message.from_user.id, message.from_user.username, bot)
    await Pm().start(message)

@dp.message_handler()
async def message_handler(message: types.Message):
    await Pm().message_handler(message)

@dp.callback_query_handler()
async def callback_query_handler(message: types.Message):
    await Pm().callback_query_handler(message) 


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
