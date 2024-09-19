# 주석(comment): 메모, 실행X

# 1. 출력함수
#    - ()값을 출력
#    - 변수값 확인 용도로 많이 활용

#    - 문자(Char) C('')
#    - 문자열(String) C("")
#    - Python은 "", '' 모두 문자열(String)
print("Hello Python")
print('Hello Python')

# 참고: Escape Code(문자열과 함께 사용)
#    - 문법(/ + @)
#    - \n (한 줄 개행)
#    - \t (탭, 8칸 공백) 
print("Hello \tPython")
print("Hello \nPython")

print('Hello Python')
print('Hello Python')
print('Hello Python')
#2. 자료형(type)
#    - Python의 모든 자료형은 객체(Object)
#    - 정수형(int):1, -1, 0
#    - 실수형(float): 3.14, 0.0
#    - 문자열(String): "Hi", 'Hi'
#    - 논리형(boolean): True, False

#3. 형 변환(Type Casting)
#    - Type Casting을 사용하여 값을 원하는 자료형으로 변환
#    - int(): ()안의 값을 정수형으로 변환
#    - float(): ()안의 값을 실수형으로 변환
#    - str(): ()안의 값을 문자열형으로 변환
a = 3
b = 3.14
c = "5"
d = "5.15"
print(float(a))
print(str(a))
print(str(b))
print(int(b))
print(int(c))
print(float(c))
print(float(d))
#print(int(d)) #STR(실수) -> 정수 ERROR 발생!

#4. None Type
#    - 사용 금지!
#    - Null == None
#     -> NullPointerException(크리티컬 오류 -> 프로그램 종료)
#    - 만약 None, Null이 필요하면 ""쓰기

#5. 변수 생성 및 초기화
#    - num = 5
#    - Python은 변수 선언시 type를 지정하지 않음!(동적 타이핑 언어)
#    - =(대입연산자) -> 우측에 값을 좌측에 대입
#    - 초기화: 초기 변수를 생성하면 변수를 생성한 메모리 공간에
#             쓰레기 파일들이 존재, 변수에 값을 대입하면
#             쓰레기 파일들이 삭제(초기화) 돼고 값만 저장!
# 
# 6. 명명규칙(Naming Rule)
#    - 변수, 함수, 클래스 등의 사용자 정의 이름에 사용!
#    - 명확하고 알아보기 쉽게!
#    1. 영어 대소문자, 숫자, 특수문자(_, -)만 사용
#    2. 숫자로 시작할수 없음
#       abc123(o), 123abc(x)
#    3. 영어 대소문자 구별
#       Abc != abc != ABC
#    4. 예약어 사용 불가
#       *예약어: Python에서 미리 선점하여 사용중인 키워드
#       print, for, while, if, else, class, and, return
#       import, def, pass, ...

# 7. 네이밍 메서드
#    - 변수, 함수, 클레스 등의 사용자 정의 이름에 사용하는 기법
#    - 프로그래밍 언어별로 Naming Mehtod가 다름
#    1) PascalCase (StdunentNumber)
#    2) camelCase (stdunentNumber)
#    3) snake_case (stdunent_number)
#    4) kebab-case (stdunent-number)

#          변수         함수        클래스
# JAVA     카멜         카멜        파스칼
# PYTHON  스네이크     스네이크     파스칼

# 8. 상수
#    - 변하지 않는 수 
#    - *상수는 반드시 선언 및 초기화(고정)를 함께
#    - 전부다 대문자 사용
MAX_VALUE = 30 #상수

# 9. 동적 출력
#    - print() -> 출력(+변수)

student_num = 24
name = "홍길동"
print("조선대학교 24학번 홍길동입니다.") # 하드 코딩(지양)
#    1. format() - old
print("조선대학교 {}학번 {}입니다.".format(student_num, name))
#    2. f-string - new
print(f"조선대학교 {student_num}학번 {name}입니다.")
