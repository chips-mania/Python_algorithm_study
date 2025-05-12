# 바구니 뒤집기

# N, M 입력 및 리스트 초기화
N, M = map(int, input().split())
basket = list(range(1, N+1))

# i, j 입력 받아서 슬라이싱 및 리스트 뒤집기
for _ in range(M):
    i, j  = map(int, input().split())

    # [start:end:-1] start와 stop을 생략하면 전체 뒤에서 앞으로를 의미
    # basket[i-1:j][::-1] -> i-1에서 j까지 슬라이싱 후 뒤집음 
    # [i:j]가 아닌 [i-1:j]임을 주의
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)