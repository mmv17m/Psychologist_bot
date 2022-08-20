import config
import db

import classes.modes.basic as basic

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Interview(basic.Basic):

	user = ""
	count = 0
	result = 0

	questions = config.INTERVIEW
	answers = config.INTERVIEW_RESULT

	def __init__(self, user):
		self.user = user
		self.count = 0
		self.result = 0

	def __get_answer(self, score):
		answer = ""
		for k, v in self.answers.items():
		    if score<=k:
		        answer = v
		        break
		return answer


	async def __step(self):
		try:
			menu = InlineKeyboardMarkup()
			question = self.questions[self.count]
			for i in range(len(question[1])):
			    menu.add(InlineKeyboardButton(text = question[1][i], callback_data = str(i)))

			await self.user.send(question[0], menu)
		except:
        
			db.set_interview_score(self.user.my_id, self.result)
			await self.user.send(self.__get_answer(self.result))
			await self.user.switch_mode("last_question")


	async def start_working(self):
		await self.__step()


	async def callback_query_handler(self, mess):
		self.count += 1
		self.result += int(mess.data)

		await self.user.delete_message(mess.message.message_id)
		await self.__step()