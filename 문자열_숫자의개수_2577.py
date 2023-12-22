a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))
answer = [0 for _ in range(10)]

for i in result:
    answer[int(i)] += 1

print(*answer, sep="\n")