line = list(input())
letter = {}

idx = 0
for c in line:
    letter[c] = idx
    idx += 1

# 알파벳 'a'부터 'z'까지의 인덱스를 출력
for char in range(ord('a'), ord('z') + 1):
    print(letter.get(chr(char), -1), end=' ')