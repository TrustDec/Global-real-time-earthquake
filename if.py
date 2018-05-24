number = 50
guess = int(input("输入一个整数:"))
if guess == number:
	print("恭喜你，你猜对了。")
	print("但你不会赢得任何奖品！）")
elif guess < number:
	print('不，这比它高一点')
else:
	print("不，这比它低一点")
print("Done")
