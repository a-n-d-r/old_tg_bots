from telethon.sync import TelegramClient

api_id = input("Введите api_id: ")
api_hash = input("Введите api_hash: ")

with TelegramClient('auth', api_id, api_hash) as client:
	dialogs = client.get_dialogs()
	print("===")
	for i in range(20):
		print(dialogs[i].title,"=",dialogs[i].id)	
input()
