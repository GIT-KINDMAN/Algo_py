# 배운점1) for key, value in -dict-.items()
# 배운점2) 리스트에도 max함수 적용 가능한거 잊지말자
# 배운점3) java랑 달리 dict에 냅다 dict[c] 박으면 c가 key가 된다.
# 결론) 자바 적 사고에 너무 갇혀 있으니, ps할 때 만큼은 파이썬 적인 사고에 더욱 노력을 기울일 것

line = input().upper()
freq = {}

for c in line:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# 위 부분까지, c라는 key에 대해 freq[c] 값이 책정되는 부분

mx = max(freq.values())

mx_alp = [key for key, value in freq.items() if value == mx]

if len(mx_alp) == 1:
    print(mx_alp[0])
else:
    print('?')