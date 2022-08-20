import os

import db

import classes.modes.basic as basic

from google.cloud import dialogflow
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


class Dialogue(basic.Basic):

	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'psylogbot.json'

	tokenizer = RegexTokenizer()
	model = FastTextSocialNetworkModel(tokenizer=tokenizer)

	

	PROJECT_ID = 'psylogbot-mipg'
	SESSION_ID = 'sessions'
	LANGUAGE_CODE = 'ru'

	user = ""
	client = ""
	SESSION = ""
	

	def __init__(self, user):
		self.user = user
		self.client = dialogflow.SessionsClient()
		self.SESSION = self.client.session_path(self.PROJECT_ID, self.SESSION_ID)

	async def start_working(self):
		await self.user.send("Напишите приветствие", {'remove' : 'Нaчать диалог','append' : "Зaкончить диалог"})


	async def finish_working(self):
		await self.user.send("Диалог завершен", {'remove' : "Зaкончить диалог"})

	async def message_handler(self, mess):

		try:
			if self.model.predict([mess.text], k=2)[0]["negative"] >= 0.5:
				new_message = await self.user.send("Я вызываю специалиста")
				db.new_message(self.user.my_id, new_message, "Я вызываю специалиста")

				await self.user.switch_mode("waiting_help")

				return 0
			
		except:
			pass


		"""Использование Dialogflow"""
		db.new_message(self.user.my_id, mess.message_id, mess.text)
		text_input = dialogflow.TextInput(text=mess.text, language_code=self.LANGUAGE_CODE)
		query_input = dialogflow.QueryInput(text=text_input)
		response = self.client.detect_intent(session=self.SESSION, query_input=query_input)

		if response.query_result.fulfillment_text:
			new_message = await self.user.send(response.query_result.fulfillment_text)
			db.new_message(self.user.my_id, new_message, response.query_result.fulfillment_text)
		else:
			new_message = await self.user.send("Я тебя не понимаю")
			db.new_message(self.user.my_id, new_message, "Я тебя не понимаю")

