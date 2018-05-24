x = 50 
def func(x):
	print('x 是',x)
	x = 2
	print('改变局部x',x)
func(x)
print('x 还是',x)