# N*N 행렬 A가 있다. 행렬의 각 원소는 1 이상 N*N 이하의 자연수로 모두 서로 다르다. 이 문제에서는 i행 j열의 원소를 A[i,j]로 표기한다.
# 당신은 이 행렬을 정렬하고자 한다. 행렬이 정렬되었다는 것은, 모든 1<=i,j<=N에 대해 A[i,j]=(i-1) x N + j가 성립한다는 것이다. 
# 이를 위해 당신은 아래 연산을 원하는 만큼 (0회 포함) 반복할 수 있다.

#     ·1 이상 N이하의 정수 x를 고른다.
#     ·1행 ~ x행, 1열 ~ x열에 해당하는 x*x크기의 부분행렬을 전치(transpose)시킨다. 그러면, 모든 1<= i,j <=x에 대해, A[i,j]는 기존A[j,i]의 값으로 바뀐다.

# 이러한 방식으로 정렬 가능한 행렬 A가 주어졌을 때, A를 정렬하기 위해 연산을 최소 몇 회 사용해야 하는지 구하는 프로그램을 작성하라


# 입력
# 첫 번째 줄에 테스트 케이스의 수 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 행렬의 크기 N(4<=N<=64)가 주어진다. 다음 N개 줄에는 행렬의 각 원소가 주어지는데, 이 중 i번째 줄의 j번째 자연수가 A[i,j]이다.
# 테스트 케이스의 개수는 2000개 이상으로 상당히 많음에 유의하라.


# 출력
# 각 테스트 케이스마다, A를 정렬하기 위해 사용해야 하는 연산의 최소 횟수를 한 줄에 하나씩 출력한다.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/21131/1_sample_input.txt","r")  

T = int(input())
answers = []

for _ in range(T):
    N = int(input())
    first_row = list(map(int, input().split()))

    # 정렬 가능한 행렬이므로 첫 번째 행만으로 전치 여부를 알 수 있다.
    for _ in range(N - 1):
        input()

    flipped = False
    count = 0

    for x in range(N, 1, -1):
        wrong = first_row[x - 1] != x
        if wrong != flipped:
            count += 1
            flipped = not flipped

    answers.append(str(count))

print('\n'.join(answers))
