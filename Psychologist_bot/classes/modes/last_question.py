import db

import classes.modes.basic as basic

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Last_question(basic.Basic):
	user = ""
	__answer = -1

	def __init__(self, user):
		self.user = user

	async def __result(self):
		if self.user.last_question_answer == -1:
			self.user.last_question_answer = self.__answer

			db.set_answer_before(self.user.my_id, self.__answer)
			await self.user.send("Начните диалог", {"append" : "Нaчать диалог"})
		else:
		    db.set_answer_after(self.user.my_id, self.__answer)
		    if self.__answer > self.user.last_question_answer:
		        await self.user.send("Ваше психоэмоциональное состояние стало лучше. Мы рады, что смогли Вам помочь.")
		    elif self.__answer == self.user.last_question_answer:
		        await self.user.send("Ваше психоэмоциональное состояние не изменилось. Рекомендуем пообщаться ещё раз.")
		    else:
		        await self.user.send("Ваше психоэмоциональное состояние стало хуже. Нам очень жаль, что так произошло. Рекомендуем обратиться к психологу.")

	async def start_working(self):
		menu = InlineKeyboardMarkup()
		for i in range(11):
			menu.insert(InlineKeyboardButton(text = i, callback_data = str(i)))
		await self.user.send("Оцените свое состояние:", menu)

	async def callback_query_handler(self, mess):
		self.__answer = int(mess.data)
		await self.user.delete_message(mess.message.message_id)
		await self.__result()