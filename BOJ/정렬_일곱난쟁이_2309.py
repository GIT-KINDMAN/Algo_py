# 출력 형식 신경 안썼다가 맞왜틀 헛고생함... 줄바꿈이었다. 주의하자

arr = []
for _ in range(9):
    arr.append(int(input()))

diff = sum(arr) - 100
arr.sort()


def func():
    for i in range(8):
        if arr[i] >= diff:
            break

        for j in range(i+1, 9):
            sum = arr[i] + arr[j]
            if sum == diff:
                return i, j
            elif arr[j] >= diff:
                break


a, b = func()
arr.pop(b)
arr.pop(a)

print(*arr, sep="\n")