
d = {'name1':'id1', 'name2':'id2', 'name3':'id3'}

inverse = {}
for key,val in d.items():
	inverse[val] = key
print(inverse)
