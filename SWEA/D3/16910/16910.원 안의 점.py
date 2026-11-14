# N이 주어질 때, 원점을 중심으로 반지름이 N인 원 안에 포함되는 격자점(x,y 좌표가 모두 정수인 점)의 개수를 구하는 프로그램을 작성하라.
# 다시 말하자면, x^2+y^2<=N^2인 격자점의 개수를 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1<=N<=200)이 주어진다.


# [출력]
# 각 테스트 케이스마다 반지름이 N인 원 안에 포함되는 격자점의 개수를 출력한다.


import sys
sys.stdin = open('/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/16910/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    answer = 0

    # 원을 둘러싼 정사각형의 모든 정수 좌표를 확인
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x * x + y * y <= N * N:
                answer += 1

    print(f'#{tc} {answer}')
