# N(바구니 개수), M(공을 넣는 횟수) 입력
N, M = map(int, input().split())

# N개의 바구니를 0으로 초기화
basket = [0]*N

# M회 공을 넣음
for _ in range(M):

    # i, j, k 입력
    i, j, k = map(int, input().split()) 

    # 바구니리스트에서 i번부터 j번 까지의 값을 k로 채움
    for x in range (i -1, j):
        basket[x] = k

# 출력
print(*basket)


# 슬라이싱과 리스트 곱셈을 활용할 수 있음
# 리스트를 분할해서 [k, ... ,k] 
# 리스트의 개수(j-(i+1))만큼 덮어씀
# basket[i-1:j] = [k] * (j - i + 1)