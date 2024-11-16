MOD = 10**9 + 7

n = int(input("Введите количество линейных функций (n): "))
m = int(input("Введите количество удалённых функций (m): "))

coeff = []
print("Введите коэффициенты линейных функций:")
for i in range(n):
    a = int(input(f"Коэффициент a_{i+1}: "))
    b = int(input(f"Коэффициент b_{i+1}: "))
    coeff.append((a, b))

removed_functions = [-1] * n
print("Введите индексы удалённых функций:")
for i in range(m):
    idx = int(input(f"Индекс {i+1}-й удалённой функции: ")) - 1
    removed_functions[idx] = 1

num_roots = int(input("Введите количество потенциальных корней: "))
roots = []
print("Введите потенциальные корни:")
for i in range(num_roots):
    root = int(input(f"Корень {i+1}: "))
    roots.append(root)

for root in roots:
    x = root
    valid = True
    
    for i in range(n):
        if removed_functions[i] == -1:
            x = (coeff[i][0] * x + coeff[i][1]) % MOD
    
    if x != 0:
        valid = False
    
    if valid:
        print(f"Найдён подходящий корень: {root}")
        exit()

print("Подходящий корень не найден")
