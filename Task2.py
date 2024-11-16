import sys

print("Пожалуйста, введите количество элементов n и количество элементов для суммы m, а затем значения стоимости через пробел:")

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
costs = list(map(int, data[2:]))

if len(costs) != n:
    print("Ошибка: количество введенных значений не соответствует n.")
    sys.exit(1)

indexed_costs = sorted((cost, index) for index, cost in enumerate(costs))

min_cost = float('inf')
min_distance = float('inf')

for i in range(n - m + 1):
    total_cost = sum(cost for cost, idx in indexed_costs[i:i + m])
    if total_cost < min_cost:
        min_cost = total_cost
        min_distance = indexed_costs[i + m - 1][1] - indexed_costs[i][1] + 1

print(f"Минимальное расстояние между элементами, сумма которых минимальна: {min_distance}")
