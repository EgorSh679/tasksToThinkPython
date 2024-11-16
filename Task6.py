from math import gcd

m, n, q = map(int, input("Введите три числа m, n и q (через пробел): ").split())
print("Введите элементы массива X длиной n:")
X = list(map(int, input().split()))
print("Введите элементы массива Y длиной m:")
Y = list(map(int, input().split()))

print("Введите запросы:")
for _ in range(q):
    query = list(map(int, input().split()))
    t = query[0]

    if t == 1:
        k = query[1]
        numerator = Y[(k - 1) % m]
        denominator = X[(k - 1) % n]
        divisor = gcd(numerator, denominator)
        print(numerator // divisor, denominator // divisor)

    elif t == 2:
        i, v = query[1], query[2]
        X[i - 1] = v

    elif t == 3:
        i, v = query[1], query[2]
        Y[i - 1] = v
