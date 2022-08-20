
import classes.modes.basic as basic
import classes.person_manager as pm

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
class Waiting_request(basic.Basic):

	async def take_call(self, user_id):
		menu = InlineKeyboardMarkup()
		menu.add(InlineKeyboardButton(text = "Ответить", callback_data = str(user_id)))
		mess = await self.user.send("Вас вызывают.", menu)
		return mess

	async def callback_query_handler(self, mess):
		await pm.Person_manager().connect(mess.data, self.user.my_id)
		