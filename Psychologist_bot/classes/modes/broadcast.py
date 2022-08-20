import db
import classes.modes.basic as basic



class Broadcast(basic.Basic):

	companion = ""
	user = ""

	def __init__(self, user, companion):
		self.user = user
		self.companion = companion

	async def start_working(self):
		print(self.user.my_id,self.user.buttons)
		await self.user.send(f"Вас соединили с {self.companion.name}", {'append' : "Зaвершить разговор"})


	async def message_handler(self, mess):
		if mess.text == "Зaвершить разговор":
			await self.user.send("Диалог завершен", {"remove" : "Зaвершить разговор"})
			await self.companion.send("Диалог завершен", {"remove" : "Зaвершить разговор"})
			await self.companion.start(mess)
			await self.user.start(mess)
		else:
			db.new_conversation_message(self.user.my_id, self.companion.my_id, [mess.message_id, self.user.my_id, mess.text])
			await self.companion.send(mess.text)