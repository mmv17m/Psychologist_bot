import classes.persons.person as person


class User(person.Person):

	#смотрите класс person

	last_question_answer = -1

	keyboard_commands = {
		"Нaчать диалог" : "dialogue",
		"Зaкончить диалог" : "last_question",
		"Вызвать службу поддержки" : "waiting_help"
	}

	async def start(self, mess):
		await self.send("""
    	    Чат-бот психолог PsylogBot
    	    Автор: @MedvedevKWORK
    	""", {'append' : "Вызвать службу поддержки"})

		await self.switch_mode("interview")
