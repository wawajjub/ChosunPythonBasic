# 조건문(Condition): if~elif~else
#    - 특정조건을 만족하는 경우 수행할 작업에 사용
#    - 모든 블록문의 마지막 :(콜론) 사용

# if 조건1:
#     code
# elif 조건1:
#     code
# elif 조건1:
#     code
# else:
#     code

# if문 조합식
#   1. if
#   2. if~else
#   3. if~elif
#   4. if~elif~else

# 논리 연산자: AND, OR, NOT
#    - AND: 두 조건이 모두 참인 경우에만 참
#    - OR: 하나의 조건이라도 참이면 참
#    - NOT: 참이면 거짓, 거짓이면 참

# 예제: 태어난 연도를 입력하면 [성인, 대학생, 고등학생, 중학생, 초등학생, 어린이] 출력하는 코드작성

# input() -> 키보드 값 전달받음
#    - 문자열 형으로 입력받음
from datetime import datetime
now = datetime.today().year 
born = int(input("태어난 년도: ")) # 사용자의 출생년도 입력
if (now<born):
    print("출생년도를 잘못입력하셨습니다.")
age= now-born
print(age)
if(age > 26):
    category = "성인"
elif(age > 19):
    category ="대학생"
elif(age > 16):
    category ="고등학생"
elif(age > 13):
    category ="중학생"
elif(age > 8):
    category ="초등학생"
elif(age > 0):
    category ="어린이"
else:
    print("잘못 된 계산입니다.")
    
print(f"당신의 출생년도는 {born}년으로 {age}살이고 {category}입니다.")