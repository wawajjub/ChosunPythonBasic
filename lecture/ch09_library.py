# 라이브러리(Library), 패키지(Package), 모듈(Module)
#   라이브러리 >= 패키지 >= 모듈

# *라이브러리: 외부 개발자가 개발해 놓은 코드 묶음
#   ㄴ 패키지1
#          ㄴ모듈1(.pt 1개)
#          ㄴ모듈2
#          ㄴ모듈3
#   ㄴ 패키지2
#          ㄴ모듈4
#          ㄴ모듈5
#          ㄴ모듈6
#   ㄴ 패키지3
#          ㄴ모듈7


# 사용 방법
#   - 외부에서 개발했기 때문에 프로그래밍 언어 설치하면 존재 X
#   1. 다운로드(아나콘다 pip install)
#   2. 불러오기(import 라이브러리)
#   3. 사용하기(라이브러리.math())

# * 가정: "requests" 라이브러리 내에 모듈이 1,000개 존재

# 1. import requsests
# -> 1000개 모두 불러오기
# -> requests.get()

# 2. from requests import get, post
# -> get(), post() 2개만 불러오기
# -> get()
# -> post()

# *. AS(Alias: 별명)
# import requests as req
# -> req.get