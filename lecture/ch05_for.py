# 반복문
#    1. for     -> 반복 횟수를 아는경우
#    2. while   -> 반복 횟수를 모르는경우

# 컬랙션과 함께 자주 사용!
# -> 컬랙션의 길이많큼 반복 
for num in [1,2,3]:
    print(num) 
    
# range(시작:끝:인터벌)
# range(1,5,1) -> 1, 2, 3, 4
# range(1,5,2) -> 1, 3,
# range(1,5) -> 1, 2, 3, 4 (인터벌 생략:1)
# range(7) -> 0, 1, 2, 3, 4, 5, 6 (시작: 0)

for num in range(0,11,1):
    print(num)    
    
# 반복 횟수 인덱스를 사용하고 싶은 경우
#  -> enumerate()를 사용하면 인덱스 사용 가능
a = ["A", "B", "C"]
for i, val in enumerate(a):
    print(i, val)


# 구구단 2단
# 2X1=2
# ...
# 2X9=18
for i in range(1,10):
    print(f"2x{i}={2*i}")
    
# 숙제 
# 중첩 for문을 사용해서 2단부터 9단까지 구구단 출력
for i in range(2,10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")