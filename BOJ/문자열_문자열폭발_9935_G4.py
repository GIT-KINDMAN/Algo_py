# line = input()
# bomb = input()
#
# while bomb in line:
#     line.replace(bomb, '')
#
# if line:
#     print(line)
# else:
#     print('FRULA')

# line = input()
# bomb = input()
#
# while bomb in line:
#     line.replace(bomb, '')
#
# if line:
#     print(line)
# else:
#     print('FRULA')

import sys

line = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
bomb_len = len(bomb)

for i in range(len(line)):
    stack.append(line[i])
    if stack[len(stack) - bomb_len : len(stack)] == bomb:  # 스택으로부터 역방향 배열따기. 길이 세지 말고 바로 단어로
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(*stack, sep="")
else:
    print('FRULA')