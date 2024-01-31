# 누더기 코드 ㅋㅋ

import sys

# name = ['H', 'T', 'C', 'K', 'G']
name = ['C', 'G', 'H', 'K', 'T']
num = list(map(int, sys.stdin.readline().rstrip().split()))
total = dict(zip(name, num))

# print(*total, sep=' ')
# print(num.index(max(num)))
T = int(sys.stdin.readline().rstrip())

base = 0

for i in range(T):
    # scale =

    h, t, c, k, g = list(map(int, sys.stdin.readline().rstrip().split()))

    # for key, values in range(len(total)):
    #     total[key] = total[key] - key.lower()

    if 'H' in total:
        total['H'] -= h
    if 'T' in total:
        total['T'] = total['T'] - t
    if 'C' in total:
        total['C'] = total['C'] - c
    if 'K' in total:
        total['K'] = total['K'] - k
    if 'G' in total:
        total['G'] = total['G'] - g

    eli = [key for key, value in total.items() if value == 0]

    for key in eli:
        total.pop(key)

    total = dict(sorted(total.items(), key=lambda x: (-x[1], x[0])))

    keys = list(total.keys())
    values = list(total.values())

    _k = ''.join(keys)
    _sum = sum(values)

    result = ''

    if not base == 0 or base == 1:
        while _sum > 0:
            remainder = _sum % base
            result = str(remainder) + result
            _sum //= base

        __v = str(result)
    else:
        __v = str(_sum)

    ___v = list([__v, '7', 'H'])
    _v = ''.join(___v)

    print(_v)
    print(_k)

    base = _sum % 10

    if len(total) == 0:
        print('NULL')