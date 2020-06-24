# 자료형 
 #숫자형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
# 숫자형 자료는 아무것도 하지 않아도 잘 나옴 아주 직관적임
 # 문자형
print('풍선')
print("나비")
print("ㅋ"*9)

# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))


# 애완동물을 소개해 주세요~

animal = "고양이"
name = "보름이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print( name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
#정수형은 print 문에 사용하기위해선 str()이 사용되어야함
print( name + "는 어른일까요? " + str(is_adult))

#따옴표 안에 띄어쓰기 구현해줘야함

'''주석을
여러문장 할 수 있다'''

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항"
# 출력문장 : xx 행 열차가 들어오고 있습니다.

station = "사당"

print( station + " 행 열차가 들어오고 있습니다.")
station = "신도림"
print( station + " 행 열차가 들어오고 있습니다.")
station = "인천공항"
print( station, "행 열차가 들어오고 있습니다.")

# 연산자

print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3
print(10%3) # 나머지 구하기
print(5//3) # 몫

print(10 > 3) # True

print(3 == 3) # 앞과 뒤의 값이 똑같다.

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)

number += 2
# 간소화해서 표현하는 방법

print(abs(-5)) # 절댓값
print(pow(4,2)) # 4에 2승
print(max(5,12))
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10)
print(int(random()*10))
print(int(random()*10))
print(int(random()*10))
print(int(random()*10) + 1)

print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)

print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45)) 
print(randint(1, 45)) 
print(randint(1, 45)) 
print(randint(1, 45)) 
print(randint(1, 45)) 
print(randint(1, 45)) 


#Quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.

# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#(출력문 예제) 
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *

offline = randint(4,28)
online1 = randint(4,28)
online2 = randint(4,28)
online3 = randint(4,28)

# if online1 = online2
#    online2 = print(radinet(4,28))
# else online2 == online2

# if online1 == online3
#    online3 == print(radinet(4,28))
# else online3 == online3

# if online2 = online3
#    online3 = print(radinet(4,28))
# else online3 = online3

print("오프라인 스터디 모임 날짜는 매월 " + str(offline) + " 일로 선정되었습니다.")
print("온라인 스터디 모임 날짜는 매월 " + str(online1) + "," + str(online2) + "," + str(online1) + " 일로 선정되었습니다.")

# 슬라이싱
jumin = "990120-1234567"
# 필요한 정보만 가져오는게 슬라이싱

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("일 : " + jumin[4:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 ( 뒤에 부터 ) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

#문자열 함수

python = "Python is Amazing"
print(python.lower()) #소문자로 변환
print(python.upper()) #대문자로 변환
print(python[0].isupper()) # 0번째 숫지가 대문자니?
print(len(python)) # 변수 문자 길이
print(python.replace("Python", "Java")) # 지정 변환

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Python")) # 위치반환
print(python.find("Java")) # -1 이 나오면 해당 문자열 없음
# print(python.index("Java")) # 없으면 그냥 오류 뜸

print(python.count("n"))

# 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # %d는 숫자형 
print("나는 %s을 좋아해요." % "파이썬") # %s는 문자형
print("Apple 은 %c로 시작해요." % "A") # %C는 문자 한개
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20)) 
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자

print("백문이 불여일견\n백견이 불여일타") # \n은 줄바꿈

# 저는 "김범수" 입니다.
print("저는 \"김범수\" 입니다.") #""를 구현하는 법, 앞에 \넣기

# \\ : 문장 내에서 하나의 역슬러쉬 표현

print("C:\\Users\\kbs03\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 이동해서 그 뒤 내용을 덮어씀

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

# Quiz ) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수  + "!" 로 구성

# 예 ) 생성된 비밀번호 : nav51!

# 나의 풀이
site = "http://naver.com"
a = site.find(".")
site = site[7:a]
print(site[0:3])
print(len(site))
print(site.count("e"))
eng = site[0:3]
leng = len(site)
counte = site.count("e")
warn = "!"
print(f"생성된 비밀번호 : {eng}{leng}{counte}{warn}")

# 나도코딩 풀이

url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1
#print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2
# 따로 변수 선언 할 필요없이 구문 내에 인덱스 넣으면 됨
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 총평 : 변수 선언을 많이 한다고 좋은게 아니다. 가능한 간단하게 코딩하는 연습을 하자
# 문자열로 바꾸는것에 익숙해지자 str()

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호씨 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명있는 지 확인

subway.append("유재석")
print(subway.count("유재석"))

# 정렬도 가능 
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용

num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) 캐비넷에 5라는 키가 없기 때문에 프로그램 종료
print(cabinet.get(5)) # 키가 없으면 none 출력
print(cabinet.get(5, "사용가능")) # none 대신에 다른 값 지정해서 출력 가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

# KEY 들만 출력

print(cabinet.keys())

# value 들만 출력

print(cabinet.values())

# 둘 다 출력

print(cabinet.items())

# 목욕탕 폐점

cabinet.clear()
print(cabinet)

#튜플 : 변경이 허용되지 않으나 리스트보다 처리 속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", "20", "코딩")
print(name, age, hobby)

# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "조세호", "양세형"}
python = set(["유재석","박명수"])

# 교집합 (java 와 python을 모두 할 수 있는 사람)

print(java & python)
print(java.intersection(python))

# 합집합 ( java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 ( java는 할 수 있지만 python은 못 하는 개발자)
print( java - python )
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("유재석")
print(java)

# 자료구조의 변경
# 커피숍

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

#조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

#(출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 :1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --

#(활용 예제)
#from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst,1))

# 나의 풀이
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(id)
shuffle(id)
chicken = sample(id,1)
id = set(id)
chicken2 = set(chicken)
id = id.difference(chicken2)
coffee = sample(id,3)

print(id)
print(f" -- 당첨자 발표 --\n치킨 당첨자 : {chicken}\n커피 당첨자 : {coffee}\n -- 축하합니다. --")

# 나도코딩 풀이
from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
users = list(users)
shuffle(users)

winners = sample(users, 4) # 4명 중에 1명은 치킨 3명은 커피

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다. --")

# 또 다시 복잡한 풀이를 했다. 변수 선언에 집착하지 말고 안쪽에서 해결하도록 하자 
# 4명을 뽑아 놓고 배분하는 방법이 더 간단 



