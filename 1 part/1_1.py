x = int (input('Введите вклад в банке'))
p = int (input('Введите процент вклада'))
y = int (input('Введите максимальную сумму вклада'))
i = 0
while x<y:
	x = x + int(x*p/100)
	print(x)
	i = i+1
print(i)




