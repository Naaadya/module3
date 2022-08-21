
login = input('Введите логин')
passwd = input('Введите пароль')
import json
def register(login,passwd):
	#name = {}
	with open ('users.json','r') as f:
		name = json.load(f)
	if login in name.keys():
		print('Введите новый логин')
	else:
		name[login] = passwd
		with open ('users.json','w') as f:
			json.dump(name,f)
		print('Регистрация успешна')

	
register(login,passwd)


