import sys

N, K = map(int, input().split(" "))

arr = [i for i in range(2, N + 1)]

count = 0
for i in range(2, N+1):
    mod_val = arr[0]
    count += 1

    if count == K:
        print(mod_val)
        sys.exit(0)

    list = [0]

    for j in range(1, len(arr)):
        if arr[j] % mod_val == 0:
            count += 1

            if count == K:
                print(arr[j])
                sys.exit(0)

            list.append(j)

    for k in range(len(list)-1, -1, -1):
        arr.pop(list[k])