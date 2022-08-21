
import json


def login_function2(login, passwd):
	with open ('users.json','r') as f:
		name = json.load(f)
	if login not in name.keys():
		print('Неверный логин')
		return
	if name[login] != passwd:
		print('Неверный пароль')
		return
	print('Вход успешен')

login = input('Введите логин')
passwd = input('Введите пароль')
login_function2(login, passwd)