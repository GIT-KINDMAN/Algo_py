# 반성점)
# remove는 O(2N)이니까, 상수 시간 줄여보겠다고 remove()대신 pop()을 쓰겠다고 인덱스 접근을 했다.
# 좋은 생각이었지만, 뒤에서부터 탐색해서 바로 지우게 되면 2 4 6을 지우는게 아니라 6 4 2를 지우게 돼서 순서가 꼬인다.
# 그래서, 제대로 제출할 때에는 따로 list를 만들어 index에 저장해두고, 거기서 for문을 N-1부터 0까지 돌려 삭제했다.

import sys

N, K = map(int, input().split(" "))

arr = [i for i in range(2, N + 1)]

count = 0
for i in range(2, N):
    mod_val = arr[0]
    arr.pop(0)
    count += 1
    print()
    print(f"i={i}: {len(arr)}, {arr}")
    print()
    for j in range(len(arr)-1, 0, -1):
        print(f"j: {j}")
        if arr[j] % mod_val == 0:
            count += 1
            print(f"arr[j]_val: {arr[j]}, count: {count}")

            if count == K:
                print()
                print(arr[j])
                sys.exit(0)

            arr.pop(j)