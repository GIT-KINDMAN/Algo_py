#  문제 파악을 잘못했다. '인쇄를 할 경우'에만 카운팅 하는 것. 너무 복잡하게 생각했다.

from collections import deque
import sys

TC = int(input())

for _ in range(TC):

    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    q = deque()
    max_arr = []

    wasted = arr[M]

    for i in arr:
        q.append(i)
        max_arr.append(i)

    max_arr.sort() #  크기 비교용. 메모리 희생, 시간 상승. 가장 큰 값인 [-1]을 기준으로 비교할 것임

    print(f"wasted: {wasted}")

    print(f"q: {q}")
    print(f"max_arr: {max_arr}")
    print(f"max_arr[-1]: {max_arr[-1]}")

    count = 0
    while q:
        val = q.popleft() #  이번에 뽑힌 문서의 우선순위
        count += 1
        if val == wasted:
            break
        elif val >= max_arr[-1]: # 뽑힌 애가 제일 우선순위 높으면, 다시 추가해 줄 필요는 없음
            print(f"qq: {q}")
        elif val < max_arr[-1]:
            q.append(val)

    # print(count)
