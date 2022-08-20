import classes.modes.basic as basic
import classes.modes.interview as interview
import classes.modes.dialogue as dialogue
import classes.modes.last_question as last_question
import classes.modes.waiting_help as waiting_help
import classes.modes.broadcast as broadcast
import classes.modes.waiting_request as waiting_request




class Mode_switch(basic.Basic):

	modes = {
		"basic" : basic.Basic,
		"interview" : interview.Interview,
		"dialogue" : dialogue.Dialogue,
		"last_question" : last_question.Last_question,
		"waiting_help" : waiting_help.Waiting_help,
		"broadcast" : broadcast.Broadcast,
		"waiting_request" : waiting_request.Waiting_request
	}

	__mode = "" 
	__text_mode = ""

	user = ""

	def __init__(self, user):
		self.user = user

		self.switch_mode("basic")

	def get_mode(self):
		return self.__text_mode

	def switch_mode(self, mode, argument = None): #я знаю про *args и **kwargs, если нужно передать несколько делайте словарь
		try:
			if argument:
				self.__mode = self.modes[mode](self.user, argument)
			else:
				self.__mode = self.modes[mode](self.user)
			self.__text_mode = mode
		except:
			print(f"Режим {mode} не найден")

	async def take_call(self, user_id):
		return await self.__mode.take_call(user_id)

	async def start_working(self):
		await self.__mode.start_working()

	async def finish_working(self):
		await self.__mode.finish_working()

	async def message_handler(self, mess):
		await self.__mode.message_handler(mess)

	async def callback_query_handler(self, mess):
		await self.__mode.callback_query_handler(mess)