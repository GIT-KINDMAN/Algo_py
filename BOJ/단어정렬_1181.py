# 기록)
# 1. String을 받을 때, readline으로 받더라도 split()을 하지 않으면 word가 'word'가 아닌 ['w','o','r','d']가 된다.
# -> 그러니 split()을 써야한다
# 2. for 문 내에서 중복을 거를때도, 단순히 readline으로 받은 line을 in list 체크를 해선 안된다.
# -> 원소를 체크해야 하는 것이기 때문에, 2중 for문을 돌리거나, list를 그냥 다 받고 set으로 만들어 중복 제거 처리를 해주자

import sys

N = int(sys.stdin.readline().rstrip())

list = []

for _ in range(N):
    list.extend(sys.stdin.readline().rstrip().split())

unique = set(list)

answer = sorted(unique, key=lambda x: (len(x), x))

print(*answer, sep="\n")