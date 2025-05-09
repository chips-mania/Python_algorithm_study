# 과제 안 내신 분..?

# StudentNumbers는 [1, 2, ... , 30]
StudentNumbers = list(range(1, 31))

# 28회 숫자를 입력받아서 반복
for _ in range(1, 29):
    n = int(input())

    # 입력받은 학생의 번호가 StudentNumbers에 존재한다면
    if n in StudentNumbers:

        # 리스트에서 해당 번호를 삭제
        StudentNumbers.remove(n)

# 제출한 출석번호를 제외한 번호를 한 줄씩 출력
for num in StudentNumbers:
    print(num)


