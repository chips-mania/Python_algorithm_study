# 공 바꾸기

# N(바구니 개수), M(공을 바꾸는 횟수) 입력
N, M = map(int, input().split())

# LIST CONPREHENSION
# N개의 바구니를 초기화
# range(N) : 만약 바구니 개수가 N개 일 경우 0, 1, ... , N-1
# range(N)에서 i를 하나씩 꺼내서 basket이라는 리스트에 넣어줌 
# basket은 [1, 2, ... , N]
basket = [i + 1 for i in range(N)]

# M회 공을 교환
for _ in range(M):

    # i, j 입력
    i, j = map(int, input().split())
    
    # a, b = b, a : 교환
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# 출력
print(*basket)

