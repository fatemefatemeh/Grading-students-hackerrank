L = []
for i in range(5):
    x = int(input('please inter a number :'))
    if 100 < x or x < 0:
        print('it is a wrong number, please insert a number between 0 and 100')
    else:
        L.append(x)
print(L)

for g in L:
    z = g // 10
    x = g % 10
    if x <= 5:
        t = z * 10 + 5
    else:
        t = z * 10 + 10

    u = t - g
    if g < 38:
        print(g)
    elif u <3:
        print(t)
    else:
        print(g)


