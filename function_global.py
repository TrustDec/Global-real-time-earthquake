x = 50
def func():
	global x
	print('x is',x)
	x = 2
	print('改变全局x为',x)
func()
print('x的值为',x)