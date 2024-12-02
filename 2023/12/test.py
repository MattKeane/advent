for i in range(5):
	print(i)
else:
	try:
		print(i)
	except NameError:
		print('name error')
