def too_old(x):
	return x > 30
ages = (22, 25, 29, 34, 56, 24, 12)
print(list(filter(too_old, ages)))
