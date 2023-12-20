#  제대로 다시 푼 것. 메모리를 좀 더 써서 시간복잡도를 줄인 부분은 유지했다.

from collections import deque
import sys

TC = int(input())

for _ in range(TC):

    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    q = deque()
    max_arr = []

    idx = 0
    for i in arr:
        q.append((i, idx))
        max_arr.append(i)
        idx += 1

    max_arr.sort()  # 크기 비교용. 메모리 희생하여 시간 상승. 가장 큰 값인 [-1]을 기준으로 비교할 것임

    count = 0
    while q:
        val, idx = q.popleft()  # 이번에 뽑힌 문서의 우선순위 값 및 인덱스
        if idx == M and val == max_arr[-1]:
            count += 1
            break
        elif val == max_arr[-1]:  # 뽑힌 애가 제일 우선순위 높으면, 다시 추가해 줄 필요는 없음. 그리고 max 배열 최대값 삭제
            count += 1
            max_arr.pop(-1)
        elif val < max_arr[-1]:
            q.append((val, idx))

    print(count)
