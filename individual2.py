import random
k = random.randint(1, 180)
print(k)
list = [i for i in range(10, 100)]
for i in list:
    if (k - 1) == list.index(i):
        a = (i - 10) // 2 + 1
        b = a + 9
        if k % 2 == 0:
            c = ((k // 2) - 1) % 10
        else:
            c = (k // 20) + 1
        print(a, b, c)