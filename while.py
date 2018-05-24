number = 23
running =True
while running:
    guess = int(input("输入一个整数:"))
    if guess == number:
        print('恭喜你，你猜对了。')
        running = False
    elif guess < number:
        print('不，这比它低一点。')
    else:
        print('不,这比它高一点')
else:
    print('while循环结束。')
print('Done')

