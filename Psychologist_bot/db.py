import psycopg2

import config


HOST = config.HOST
USER = config.USER
PASSWORD = config.PASSWORD
DB_NAME = config.DB_NAME 


def new_data_base():
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(
				f"""CREATE TABLE users(
					user_id text PRIMARY KEY,

					user_name text,
					interview_score integer,
					answer_before integer,
					answer_after integer
				);"""
			)

			connection.commit()
	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()


#new_data_base()
def new_user(user_id, user_name):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(
				"""INSERT INTO users (
					user_id,
					user_name)

					VALUES (%s, %s);""", [str(user_id), str(user_name)]
			)

			connection.commit()

		with connection.cursor() as cursor:
			cursor.execute(
				f"""CREATE TABLE messages_{user_id}(
					message_id text PRIMARY KEY,
					message_text text
				);"""
			)

			connection.commit()

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()


def set_interview_score(user_id, interview_score):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(f"""UPDATE users SET interview_score = %s WHERE user_id = '{str(user_id)}';""",[int(interview_score)])
			connection.commit()

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()




def set_answer_before(user_id, answer_before):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(f"""UPDATE users SET answer_before = %s WHERE user_id = '{str(user_id)}';""",[int(answer_before)])
			connection.commit()

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()

def set_answer_after(user_id, answer_after):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(f"""UPDATE users SET answer_after = %s WHERE user_id = '{str(user_id)}';""",[int(answer_after)])
			connection.commit()

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()

def new_message(user_id, message_id, message_text):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		with connection.cursor() as cursor:
			cursor.execute(
				f"""INSERT INTO messages_{user_id} (
					message_id,
					message_text)

					VALUES (%s, %s);""", [str(message_id), str(message_text)]
			)

			connection.commit()

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()


def get_table_conversation_name(p1_id, p2_id):
	table_name = f"messages_{p1_id}_{p2_id}"
	if int(p2_id)<int(p1_id):
		table_name = f"messages_{p2_id}_{p1_id}"
	return table_name


def new_conversation(p1_id, p2_id):
	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		table_name = get_table_conversation_name(p1_id, p2_id)

		with connection.cursor() as cursor:
			cursor.execute(
				f"""CREATE TABLE {table_name}(
					message_id text PRIMARY KEY,
					user_id text,
					message_text text
				);"""
			)

			connection.commit()
		

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()


def new_conversation_message(p1_id, p2_id, message):

	try:
		connection = psycopg2.connect(
			host = HOST,
			user = USER,
			password = PASSWORD,
			database = DB_NAME
		)

		table_name = get_table_conversation_name(p1_id, p2_id)

		with connection.cursor() as cursor:
			cursor.execute(
				f"""INSERT INTO {table_name} (
					message_id,
					user_id,
					message_text
					)
					VALUES (%s, %s, %s);""", [str(message[0]), str(message[1]), str(message[2])]
			)

			connection.commit()

		

	except Exception as ex:
		print("DB ERROR START", ex, "DB ERROR END")
	
	finally:
		if connection:
			connection.close()


if __name__ == "__main__":
	new_data_base()
	#new_user(0, "d")
	#new_message(0,0,"d")