#################################
## 프로젝트     : kisck_ice
## 작성자       : wawajjub
## 최초생성     : 2024년 10월 14일
## 마지막 수정  : 2024년 10월 14일
## 내용        : 아이스크림을 판매하는 키오스크의 메인 프로그램
## +회사명
## +라이센스

from service_kiosk import print_sub_menu, input_menu_num

################################
# 1. 메뉴와 가격표 생성
################################
# Dict타입 생성 -> 향후 "데이터 베이스" 사용! 
# - 메인 메뉴
main_menu = {
    1:"아이스크림", 
    2:"음료", 
    3:"디저트"
}
# - 서브메뉴
icecream_menu = {
    1:"초콜릿",
    2:"바닐라",
    3:"딸기"
}
icecream_price = {
    1: 4000,
    2: 3000,
    3: 5000
}
drink_menu = {
    1:"우유",
    2:"커피",
    3:"에이드"
}
drink_price = {
    1: 2500,
    2: 3000,
    3: 3500
}
desert_menu = {
    1:"케이크",
    2:"쿠키",
    3:"비스킷"
}
desert_price = {
    1: 25000,
    2: 3500,
    3: 2500
}

# 사용자가 주문한 메뉴목록
order_list = []

##########################
# 2. 메인메뉴 출력 
##########################
while True:
    print("*"*50)
    print("== 아이스크림 가게 ==")
    print("1. 아이스크림")
    print("2. 음료")
    print("3. 디저트")
    print(">> MSG: 메뉴를 선택해주세요.")
    
    order = input_menu_num(3)
    
    if order == 1: #서브: 아이스크림
        print_sub_menu(icecream_menu, icecream_price, 3)
        sub_order = input_menu_num(3)
        order_list.append([icecream_menu[sub_order], icecream_price[sub_order]])
    elif order == 2: #서브: 음료
        print_sub_menu(drink_menu, drink_price, 3)
        sub_order = input_menu_num(3)
        order_list.append([drink_menu[sub_order], drink_price[sub_order]])
    elif order == 3: #서브: 디저트
        print_sub_menu(desert_menu, desert_price, 3)
        sub_order = input_menu_num(3)
        order_list.append([desert_menu[sub_order], desert_price[sub_order]])
    
    # 추가 주문 or 결제
    extra_order = input("추가 주문하시겠습니까?(y/n)")
    if extra_order == 'y':
        pass
    elif extra_order == 'n':
        break

print("결제 목록")
    # 사용자가 주문한 메뉴 출력
for item in order_list:
        print(item)
        
        
    
    