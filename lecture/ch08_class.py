# 절차지향 프로그래밍 (C)
#   1. 함수를 만들고 순차적으로 프로그램이 동작하는 방식
#   2. 객체나 클래스를 만들 필요없이 바로 코딩 가능
#      (함수호출 가능, 프로그램 호출 쉽게 추적 가능)
#   3. 코드끼리 유기성이 높아 새로운 데이터나 기능 추적하기 어려움
#      (코드 재사용 불가, 유지보수 어려움) 

# 객체지향 프로그래밍 (Java, Python)
#   1. 각 객체에서 수행할 수 있는 함수와 필드를 묶어서 하나의
#      클래스를 만들고, 기능을 객체로 만들어 동작하는 방식
#   2. 캡슐화(모듈화)로 인해 유지보수 용이
#   3. 객체 자체가 하나의 프로그램이기 때문에 상속처럼 코드재사용 용이
#   4. 많은 양의 메모리 필요해서 속도가 느림, 설계하는데 시간 필요  

# Class란?
#   + 실세계의 것을 모델링하여 속성과 동작을 갖는 데이터 타입
#   + python에서는 모든 것이 객체입니다.
#    - 기본 자료형(프리미티브), 객체 자료형(레퍼런스) -> Java
#    - 객체 자료형(레퍼런스) -> python

# Object(객체)란?
#   + 클레스로 생성되어 구체화된 객체(인스턴스)
#   + 실제로 Class가 인스턴스화 되어 메모리에 상주하는 상태를 의미
#   + Class가 빵틀이라면, Object는 빵틀로 찍어낸 빵

# Class(힐스테이트 설계도면) -> 객체 생성 -> 수완동(수완 힐스테이트: 인스턴스)
# Class(힐스테이트 설계도면) -> 객체 생성 -> 동선동(봉선 힐스테이트: 인스턴스)
# Class(힐스테이트 설계도면) -> 객체 생성 -> 지산동(지산 힐스테이트: 인스턴스)

# 객체 사용 3단계
#   1. Class생성
class ChosunTest:
    # 클래스에 소속된 멤버함수는 첫번째 매개변수로 self인자를 반드시 받아야함!
    # self: 생성 된 인스턴스
    def printf_name(self, name):
        print(name)
#   2. 객체 생성(-> 인스턴스)
#    + 함수(스네이크 표기법)
#    + 생성자 함수(파스칼 표기법) -> 생성자함수는 클래스 이름과 동일한 이름을 가져야함
#    + class 작성시 생성자 함수를 생략하면 자동으로 기본생성자함수를 생성함(파이썬)
test = ChosunTest()

#   3. 인스턴스 사용
test.printf_name("손주한")

class Parent:
    def print_star(self):
        print("*")
# parent = Parent()
# parent.print_star()
class Child(Parent):
    pass
ch = Child()
ch.print_star()
#   기본자료형: 변수에 실제값이 저장 
#   객체자료형: 변수에 실제값이 위치한 주소가 저장
#   NULL: "값이없다" (X)
#         "참조할 대상이 없다" (O)

a = 4
b = a+1
print(id(a))
print(id(b))

#   모델링: 현실세계를 컴퓨터세계에 구현한 것;
#       현실세계(우체부)    ->  컴퓨터세계(우체부 Class)
#       우체부가 편지를         class 우체부:
#         배달한다                  누가 = 우체부
#                                  무엇 = 편지 
#                                  def 배달한다(누가, 무엇):
#                                       우체부가 편지를 배달한다.