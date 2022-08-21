def area(s):
	c = s.split(',')
	c.sort(reverse=True)
	res = ''.join(c)
	return res

y = input('Введите числа через запятую ')
print(area(y))




