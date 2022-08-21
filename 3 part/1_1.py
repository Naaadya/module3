import math
def area (a,b,c):
	P = (a + b + c)/2
	S = math.sqrt(P*(P - a)*(P - b)*(P - c))
	return S
	
a = int(input('Введите сторону треугольника'))
b = int(input('Введите сторону треугольника'))
c = int(input('Введите сторону треугольника'))
S = area(a,b,c)
print(S)




