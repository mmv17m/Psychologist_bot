
import classes.modes.basic as basic

import classes.person_manager as pm 

class Waiting_help(basic.Basic):

	messages = {}


	async def start_working(self):
		await self.user.send("Ожидайте", {'clear' : None})
		self.messages = await pm.Person_manager().call_assistant(str(self.user.my_id))

	async def finish_working(self):
		await pm.Person_manager().delete_messages(self.messages)