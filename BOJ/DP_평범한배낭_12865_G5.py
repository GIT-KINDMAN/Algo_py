N, K = map(int, input().split()) # N: 물품의 수, K: 배낭 허용 무게

W = [] # 각 물건의 무게
V = [] # 각 물건의 가치

for _ in range(N):
    _w, _v = map(int, input().split())
    W.append(_w) # 무게
    V.append(_v) # 가치


def knapsack(k, w, v, n):

    knap = [[0 for _ in range(K+1)] for _ in range(N+1)] # i축 보석, j축 무게

    for i in range(N+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                continue
            elif w[i-1] <= j:
                knap[i][j] = max(v[i-1]+knap[i-1][j-w[i-1]], knap[i-1][j])
                # 이전 최대 가치 vs 현재 물건 추가
            else:
                knap[i][j] = knap[i-1][j]

    return knap[n][k]


print(knapsack(K, W, V, N))