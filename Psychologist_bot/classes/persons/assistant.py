import classes.persons.person as person

class Assistant(person.Person):

	#смотрите класс person

	

	async def start(self, mess):
		await self.send("""
    	    Ожидайте запроса.
    	""")
		print("ds", self.buttons)

		await self.switch_mode("waiting_request")