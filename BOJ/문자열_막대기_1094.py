x = int(input())
binary_x = bin(x)[2:]  # 2진수로 변환 후 '0b' 접두사 제거

# 1의 개수 출력
print(binary_x.count('1'))