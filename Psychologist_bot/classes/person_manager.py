import config
import db

import classes.persons.user as user
import classes.persons.assistant as assistant

class Person_manager():

	#синглтон

	__instance = None

	all_persons = {}
	
	users = {}
	assistants = {}


	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super(Person_manager, cls).__new__(cls)
		return cls.__instance


	async def new_person(self, person_id, person_name, bot):
		if not person_id in config.ASSISTANTS:
			db.new_user(person_id, person_name)
			new_user = user.User(person_id, person_name, bot)
			self.all_persons[str(person_id)] = new_user
			self.users[str(person_id)] = new_user
		else:
			new_a = assistant.Assistant(person_id, person_name, bot)
			self.all_persons[str(person_id)] = new_a
			self.assistants[str(person_id)] = new_a


	async def call_assistant(self, user_id):
		messages = {}
		for k, v in self.assistants.items():
			mess = await v.take_call(str(user_id))
			if mess:
				messages[k] = mess
		return messages

	async def delete_messages(self, messages):
		for k, v in messages.items():
			await self.all_persons[k].delete_message(v)

	async def connect(self, p1_id, p2_id):
		db.new_conversation(p1_id, p2_id)
		p1 = self.all_persons[str(p1_id)]
		p2 = self.all_persons[str(p2_id)]
		await p1.connect(p2)
		await p2.connect(p1)

	async def start(self, mess):
		await self.all_persons[str(mess.from_user.id)].start(mess)

	async def message_handler(self, mess):
		await self.all_persons[str(mess.from_user.id)].message_handler(mess)

	async def callback_query_handler(self, mess):
		await self.all_persons[str(mess.from_user.id)].callback_query_handler(mess) 