# 三种控制流语句——if，while 和 for ——及其相关的 break 与 continue 语句
for i in list(range(5)): # range 函数生成数字序列
     # 从第一个数字开始，至第二个数字结束。
    if(i<=3):
#        break # 如果中断了一个 for 或 while 循环，任何相应循环中的 else 块都将不会被执行。
        continue
    print(i)
else:
    print('for循环结束')
