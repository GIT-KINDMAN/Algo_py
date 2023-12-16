# 기록) 사실 30이 아니라 3과 10으로 각각 분리해서 생각하면 편한 문제였다... 그냥 오기로 풀었다

N = list(input())  # 입력 값을 char[] 형태로 사용하기 위한 준비

N.sort(reverse=True)  # 리스트를 내림차순으로 정렬

for i in range(len(N)):  # 준비한 char[]의 length만큼 반복
    num = int(''.join(N))  # char을 모아 int로 변환

    if num % 30 == 0:
        print(num)
        break

    flag = False  # 바로 다음 큰 수를 찾았는지 체크하기 위한 변수

    for j in range(len(N) - 1, 0, -1):
        if N[j] > N[j-1]:  # 뒤에서부터 앞으로 탐색하며 더 작은 값이 나오면
            N[j], N[j-1] = N[j-1], N[j]  # 해당 값과 앞의 값을 교환
            N[j:] = sorted(N[j:], reverse=True)  # 교환한 위치부터 끝까지를 내림차순으로 정렬
            flag = True  # 교환이 성공했음을 표시
            break # 이제 준비된 새로운 char[]인 N을 들고 다음 loop로

    if not flag:  # 교환에 실패했다는 것은, 더 이상 보다 작은 수는 없음을 뜻함
        print(-1)  # -1 출력
        break