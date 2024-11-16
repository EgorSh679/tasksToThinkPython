N, M = map(int, input("Введите количество композиций и пожеланий (через пробел): ").split())

conditions = []
print("Введите условия:")
for _ in range(M):
    L, R, op, S = input().split()
    L, R, S = int(L), int(R), int(S)
    conditions.append((L, R, op, S))

moods = [0] * N
is_possible = True

for L, R, op, S in conditions:
    total_mood = sum(moods[L-1:R])
    if (op == '=' and total_mood != S) or \
       (op == '<' and total_mood >= S) or \
       (op == '>' and total_mood <= S) or \
       (op == '<=' and total_mood > S) or \
       (op == '>=' and total_mood < S):
        is_possible = False
        break

if is_possible:
    print("YES")
else:
    print("NO")
