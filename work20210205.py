# 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


def fun(m):
    if m == 1 or m == 2:
        return 1
    else:
        return fun(m-1) + fun(m-2)


sum = fun(6)
print(sum)