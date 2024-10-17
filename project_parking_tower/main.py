# 주차타워(엘레베이터)
#   - 1~5층(1층당 1대만 주차)
#   - 차량번호: 정수숫자 4자리만 입력

# 기능
# 1. 차량입고
# 2. 차량출고
# 3. 차량조회
# 4. 프로그램 종료

# 1. 공통 설정값
max_car = 5 # 최대 주차 5대
cnt_car = 0 #현재 주차 대수(count)

# 2. 주차타워 생성 -> list
# tower = ["", "", "", "", ""] #방법 1: 하드코딩(절대 지양)

# tower = [] #방법 2: for문 활용
# for i in range(max_car):
#     tower.append("")

#방법 3: List comprehension 활용
tower = ["" for i in range(max_car)]
# 방법2와 방법3은 똑같은 기능의 코드 
# 방법3을 사용하면 좀더 효율적으로 코드개발 가능
# 모든 for문을 "List comprehension"으로 변경불가
# (심플한 for문만 가능)

# 3. 주차타워 메뉴 출력
while True:
    print("="*50)
    print("== 주차타워 시스템 ver1.1 ==")
    print("="*50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    
    while True:
        select_num = int(input(">> 번호: "))
        if 4 >=select_num >= 1:
            break
        else:
            print(">> WARNING 올바른 값을 입력하세요.")
    
    if select_num == 1: #1. 입고
        # 도메인 지식 -> 비지니스 로직
        
        # 1. 주차타워 만차확인
        if cnt_car < max_car:
            pass
        else:
            print(">> MSG: 만차입니다. 다음에 이용해주세요.")
        # 만차y: 죄송합니다.
        # 만차n: 다음단계 이동
        # 2. 주차번호(4자리) 입력
        # + 유효성 체크(숫자만, 4자리)
        car_num = input(">> 차량번호: ")
        for i, car in enumerate(tower):
            if car == "": #빈 주차공간
                # 3. 주차타워 입고 -> tower[] 저장
                tower[i] = car_num
                # 4. 현재 주차 차량 최신화 -> cnt_car + 1
                cnt_car += 1
                break
    elif select_num == 2: #2. 출고
        # 1. 차량번호 입력(출고)
        # 2. 주차타워 주차여부 확인
        #   y: 다음단계
        #   n: "주차 되지 않은 차량입니다."
        # 3. 차량출고 -> tower -> ""변경
        # 4. 현재차량수 - 1
        scan = 0
        car_num = input(">> 차량번호: ")
        for i, car in enumerate(tower):
            if car_num == car:
                tower[i] = ""
                cnt_car -= 1
                break
            else:
                scan += 1
        if scan == 5:
            print(">> MSG: 주차 되지 않은 차량입니다.")
    elif select_num == 3: #3. 조회
        print("■"*20)
        for i in range(len(tower)):
            print(f"■■ {i+1}층: {tower[i]} ■■")
        print("■"*20)
    elif select_num == 4: #4. 종료
        print(">> MSG: 프로그램을 종료합니다.")
        exit()
    
            
        