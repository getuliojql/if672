n0, c = 1, 7

n = n0

for i in range(2, 12):
    eq1 = c * (n ** 3)
    eq2 = (3 * (n ** 3)) + (2 * (n ** 2)) + n + 1

    if 0 <= eq2 <= eq1:
        print(f'0 <= {eq2:^4} <= {eq1:^4} para n = {n}')

    n = i

n0, c1, c2 = 1, 5, 12

n = n0

for i in range(2, 12):
    eq1 = c1 * (n ** 2)
    eq2 = (5 * (n ** 2)) + (7 * n)
    eq3 = c2 * (n ** 2)

    if 0 <= eq1 <= eq2 <= eq3:
        print(f'0 <= {eq1:^4} <= {eq2:^4} <= {eq3:^5} para n = {n}')

    n = i
