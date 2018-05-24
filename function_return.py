def maximum(x,y):
	if x>y:
		return x
	elif x==y:
		return 'The numbers are equal'
	else:
		return y # 默认返回: None=虚无:用于指示一个变量没有值，如果有值则它的值便是 None（虚无）
print(maximum(2,3))

# 用于指示一个没有内容的语句块。
def some_function():
	pass

some_function()

print(max(2,3,9,0,78)) # 内置函数,尽可能地使用这一内置函数。