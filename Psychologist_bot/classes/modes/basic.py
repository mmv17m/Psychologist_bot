
class Basic:
	user = ""

	def __init__(self, user):
		self.user = user

	async def take_call(self, user_id):
		return None

	async def start_working(self):
		pass

	async def finish_working(self):
		pass

	async def message_handler(self, mess):
		pass

	async def callback_query_handler(self, mess):
		pass