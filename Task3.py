import sys

print("Пожалуйста, введите количество элементов n, а затем значения массива, разделяя их пробелами:")

input = sys.stdin.read()
data = input.split()

n = int(data[0])
a = list(map(int, data[1:]))

if len(a) != n:
    print("Ошибка: количество введенных значений не соответствует n.")
    sys.exit(1)

current_length = 1
max_length = 1

for i in range(1, n):
    if a[i] > a[i - 1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1


if max_length == 1:
    print(0)
else:
    print(max_length)
