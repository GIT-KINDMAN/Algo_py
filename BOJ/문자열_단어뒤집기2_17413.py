import sys

line = list(sys.stdin.readline().rstrip())  # 입력 받은 문자열
N = len(line)  # 공백 포함 글자 수

flag = False
answer = []
word = []
for i in range(N):
    if line[i] == '<':
        if not flag:
            word = word[::-1]
        answer.append(word)
        word = ['<']
        flag = True

    elif line[i] == '>':
        word.append('>')
        answer.append(word)
        word = []
        flag = False

    elif line[i] == ' ':
        if not flag:
            word = word[::-1]

        word.append(' ')
        answer.append(word)
        word = []
    else:  # 문자열
        word.append(line[i])

answer.append(word[::-1])
result = ''.join([''.join(word) for word in answer])
print(result)