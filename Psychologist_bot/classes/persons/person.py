import db
import classes.mode_switch as mode_switch
import classes.persons.person as person

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Person:

	__bot = ""

	my_id = 0
	name = ""

	mode = ""

	keyboard_commands = {
	}


	buttons = []

	commands_for_button = {}

	def __init__(self, user_id, user_name, bot):
		self.__bot = bot
		self.my_id = user_id
		self.name = user_name
		self.buttons = []
		self.commands_for_button = {
			'clear' : self.buttons.clear,
			'remove' : self.buttons.remove,
			'append' : self.buttons.append
		}


		self.mode = mode_switch.Mode_switch(self)

	async def switch_mode(self, mode, argument = None):
		await self.mode.finish_working()
		self.mode.switch_mode(mode, argument)
		await self.mode.start_working()

	async def get_buttons_menu(self):

		buttons_menu = ReplyKeyboardMarkup()
		for i in self.buttons:
			buttons_menu.add(KeyboardButton(i))
		if len(self.buttons) == 0:
			buttons_menu = ReplyKeyboardRemove()

		return buttons_menu


	async def send(self, text, buttons = None): #кнопки как клавиатуры, так и inline
		mess = None
		if buttons:
			if type(buttons) == dict:
				for k,v in buttons.items():
					if v:
						self.commands_for_button[k](v)
					else:
						self.commands_for_button[k]()
				mess = await self.__bot.send_message(self.my_id, text, reply_markup = await self.get_buttons_menu())

			else:
				mess = await self.__bot.send_message(self.my_id, text, reply_markup = buttons)
		else:
			mess = await self.__bot.send_message(self.my_id, text)
		mess = mess.message_id
		return mess


	async def take_call(self, user_id):
		return await self.mode.take_call(user_id)


	async def connect(self, user):
		await self.switch_mode("broadcast", user)


	async def start(mess):
		pass


	async def delete_message(self, message_id):
		await self.__bot.delete_message(self.my_id, message_id)



	async def message_handler(self, mess):
		try:
			if self.keyboard_commands[mess.text]:
				await self.switch_mode(self.keyboard_commands[mess.text])
		except:
			await self.mode.message_handler(mess)
			


	async def callback_query_handler(self, mess):
		await self.mode.callback_query_handler(mess)