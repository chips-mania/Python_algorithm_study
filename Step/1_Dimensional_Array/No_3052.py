# 나머지

# set(집합) 초기화
s = set()

# 10개 입력받아서 42로 나눈 나머지를 set에 add
for _ in range(10):
    n = int(input())
    s.add(n % 42)

# set의 길이를 세어서 print
count = len(s)
print(count)