

# 题目：输出 9*9 乘法口诀表。

for i in range(1, 10):
    print('\n')
    for j in range(1, 10):
        if(j <= i):
            print(f"{i}*{j}={i*j}", end='  ') # end=' '
        else:
            pass