# 기록)
# 중복 허용인 만큼 visited 배열은 필요 없다.
# dfs(i, depth+1)에서도 i+1가 아닌 i를 넣는다. 중복 값 허용이니까
# arr[depth] = i+1의 1은 단순히 index 때문에 [0] 값만큼 밀어준 것
# '같거나 클 것' 조건은 dfs 내의 반복문의 시작점을 v로 설정해 제한한다

N, M = map(int, input().split())

arr = [0] * M


def dfs(v, depth):
    if depth == M:
        print(*arr, sep=" ")
        return

    for i in range(v, N):
        arr[depth] = i+1
        dfs(i, depth+1)


dfs(0, 0)