MODULO = 10**9 + 7
results = []
t = int(input("Введите количество наборов красок: "))
cases = []

for i in range(t):
    n = int(input(f"Число красок в {i+1} наборе: "))
    cases.append(n)

for n in cases:
    sum_mixture = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum_mixture += i & j


    results.append(sum_mixture % MODULO)

for result in results:
    print(result)
