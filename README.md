### 1. 개발환경 구축
### 1-1. 다운로드
- anaconda
- vscode

### 1-2. 아나콘다 세팅
- conda env list                        (가상환경 목록 확인)
- conda create -n developer python=3.11 (가상환경 생성)
- conda activate developer              (가상황경 접속)
- pip list                              (설치 된 라이브러리 목록 확인)
- pip install [라이브러리]               (라이브러리 설치)
- cls                                   (화면 clear)

### 1-3. VSCODE 세팅
1. Extensions 설치
- python
- prettier
- python extension pack
- atom material icons
- atom material theme
2. Settings
- [Mouse Wheel Zoom] 켜기
3. Theme 설정
- [ctrl] + [shift] + [p] -> "python: select interp"

### 1-4. 명령어 단축키
- [ctrl] + [`] : 터미널 열기
- [ctrl] + [,] : Setting 열기
1. 기본터미널 설정
2. 터미널 폰트 사이즈 수정
3. python run 단축키 설정

### 2. 데이터베이스
데이터를 효율적으로 저장하고 관리할수있는프로그램(DBMS)

### 2-1. DBMS
- 관계형 데이터 베이스(RDB): 표형태, 보안이 중요하거나, 영속성 데이터(개인정보, 비밀번호)
    -> MariaDB, Oracle, MySQL, PostgreSQL
- NoSQL: 자유형태 대용량 수집데이터
    -> MongoDB
    
### 2-2. SQL(구조질의어)
- DBMS에 명렬을 내릴 때 사용
- 예) SELECE * FROM tbl_user;

### 2-3. DBMS 설치 방법
1. 로컬 설치
2. 클라우드 사용(AWS, GCP, Azure, 기타등등)
3. 도커 컨테이너

### 3. 도커 (컨테이너)
- 도커: 컨테이너 가상화 기술을 구현해주는 프로그램
- 도커 → 도커엔진 + 도커 이미지
- 도커 이미지: 도커 컨테이너 실행을 위한 설계도면
- 도커엔진: 도커 이미지를 바탕으로 컨테이너를 실행 

### 3-1. 도커 명령어
- docker ps: 현재 실행중인 컨테이너 확인
- docker images: 현재 보유하고있는 컨테이너 이미지 확인
- docker run: 도커 컨테이너 실행
- docker logs [컨테이너 이름]: 해당 컨테이너 로그 확인
- docker exec -it [컨테이너 이름]: 해당 컨테이너 접속
```
>> docker run --name mariadb -d -p 3306:3306 -e MARIADB_ROOT_PASSWORD=mariadb mariadb
 --name mariadb: 컨테이너 이름
 -d: 데몬(백그라운드 실행)
 -p 3306:3306: 포트(외부: 내부) → 외부포트(호스트), 내부포트(컨테이너)
 MARIADB_ROOT_PASSWORD=mariadb: 환경설정(ROOT암호=mariadb) 
 mariadb: mariadb 컨테이너 실행
```

### 99. 전체 시스템 구조(학습용) - WEB/APP
# - Client - Server 