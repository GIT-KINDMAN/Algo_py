# 딕셔너리(Map) 안쓰고 풀어본 방식
# 배운점1) ord(ordinary) 함수, chr(char) 함수. e.g. ord('A') = 65, chr(65) = 'A'

line = list(input())

freq = [0 for _ in range(26)]

for i in line:
    c = ord(i)
    if c >= 97:
        c -= 32
    c = c-65

    freq[c] += 1

mx = 0
idx = 0
cnt = 0
for i in range(len(freq)):
    if freq[i] > mx:
        mx = freq[i]
        idx = i
        cnt = 1
    elif freq[i] == mx:
        cnt += 1

if cnt == 1:
    print(chr(idx+65))
else:
    print('?')