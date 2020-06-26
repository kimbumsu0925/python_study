# # if
# weather = input("how is the weather? ")
# if weather == "rain" or weather == "snow":
#     print("bring an umbrella")
# elif weather == "fine dust":
#     print("bring a mask")
# else: 
#     print("No need to prepare")

# temp = int(input("How is the temperature? "))
# if 30 <= temp:
#     print("too hot. don't go outside")
# elif 10 <= temp and temp < 30:
#     print("nice weather")
# elif 0 <= temp < 10:
#     print("bring a coat")
# else:
#     print("too cold . don't go outside")

# for
# print ("waiting number : 1")
# print ("waiting number : 2") 
# print ("waiting number : 3") 
# print ("waiting number : 4")

# for wating_no in [1, 2, 3, 4]:
#     print("wating number : {0}".format(wating_no))

# for wating_no in range(1,6):
#     print("wating number : {0}".format(wating_no))  

# # starbucks
# starbucks = ["jane", "john","sam"]
# for customer in starbucks:
#     print("{0}, order is ready.".format(customer))

# # while
# customer = "son"
# index = 5
# while index >= 1:
#     print("{0}, order is ready. {1} times left.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("Your coffee has been disposed of.")

# # infinite loof
# customer = "son"
# index = 1
# while = True:
#     print("{0}, order is ready. {1} times.".format(customer,index))
#     index += 1

# customer = "son"
# person = "Unknown"

# while person != customer : 
#     print("{0}, order is ready.".format(customer))
#     person = input("what is your name? ")

# # continue & break
# absent = [2,5] 
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("today's class is over, {0}, follow me.".format(student))
#         break
#     print("{0}, stand up".format(student))

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# Quiz 
# 당신은 cocoa 서비스를 이용하는 택시기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야합니다.

#(출력문 예제)
#[o] 1번째 손님 (소요시간 : 15분)
#[ ] 2번째 손님 (소요시간 : 15분)
#[o] 3번째 손님 (소요시간 : 15분)
#...
#[] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# 나의 풀이
# 승객 50명 난수로 탑승시간 지정
# if 문으로 탑승시간에 따라 "o"나  ""으로 지정 후 탑승승객 변수 += 처리
# while 문으로 1번째 손님 ~ 50번째 손님 후 총 탑승 승객 : {} 분 으로 마지막 프린트

# from random import *
# time = int(randrange(5,51))
# bording = 0
# customer = 50
# sign = ""
# while customer >= 1:
#     time = int(randrange(5,51))
#     if 5 <= time <= 15:
#         sign = "o"
#         bording += 1
#     else :
#         sign = "" 
#     print("[{0}], {1}번째 손님 (소요시간 : {2}분".format(sign,customer,time))
     
#     customer -= 1
#     if customer == 0:
#         print("총 탑승 승객 : {0}분".format(bording))

# #나도코딩 풀이
# from random import *
# cnt = 0 # 총 탑승객 수
# for i in range(1,51): 
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[o], {0}번째 손님 (소요시간 : {1}분".format(i,time))
#         cnt += 1
#     else :
#         print("[ ], {0}번째 손님 (소요시간 : {1}분".format(i,time))
     
# print("총 탑승 승객 : {0}분".format(cnt))

# # for문과 while문의 차이를 이해하고 더 유용한걸 사용할 생각해야함
# # 코드는 되도록 간결하게 짧게 쓰려는 연습을 해야함
# # 변수를 굳이 for문 전에 전부 선언할 필요 없음
# # i를 for 문에서 선언하면서 customer를 따로 선언할 필요 없음 간편!

# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()
# # 함수는 정의 만으로는 출력되지 않음 다음에 불러와야 출력

# def deposit(balance,money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:# 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commission,balance))

# 함수 기본값
# def profile(name, age, math_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, math_lang))

# profile("유재석","20","파이썬")

# def profile(name, age=17, math_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, math_lang))

# profile("유재석")
# profile("김태호")

# # 키워드 값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang = "파이썬", age = "17")

# 가변인자를 이용한 함수 호출

# def profile(name, age, lang1, lang2, lang3, lang4, lang5)
#     print("이름 : {0}\t나이: {1}\t".format(name,age),end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)
# # 언어를 5개 까지 밖에 못쓰는 함수 이때 가변인자 사용

# def profile(name, age, *language):
#     print("이름 : {0}\t나이: {1}\t".format(name,age),end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석","20","파이썬","자바","c","c++","c#","javascript")

# 지역변수와 전역변수

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# # 함수 내에 gun이 정의 되지 않음 여기서 전역변수 활용을 위해 global 사용

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# # 일반적으로 사용하지 않음 
# gun = 10
# def checkpoint_ret(gun, soldiers): # 경계근무    
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준체중을 구하는 프로그램을 작성하시오 
# * 표준 체중 : 각 개인의 키에 적당한 체중

#( 성별에 따른 공식)
 # 남자 : 키(m) x 키(m) x 22
 # 여자 : 키(m) x 키(m) x 21
# 조건 1: 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리 까지 표시

# #(출력 예제)
# #키 175cm 남자의 표준 체중은 67.38kg 입니다.
 
# def std_weight(height, gender):
#     if gender == "man":
#         weight = round(height * height * 22 / 10000,2)
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,weight))
#     elif gender == "woman":
#         weight = round(height * height * 21 / 10000,2)
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,weight))

# std_weight(175, "woman")

# #나도코딩 풀이 
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22        
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight =round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))
## 남자가 아닌 다른 아무말이나 써도 여자 표준체중을 구하게 되는 케이스 함수안에 프린트 구문도 넣는게 좋지 않나?

#표준입출력

# print("Python", "Java", end = "?") # end의 디폴트는 줄바꿈 
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():#items를 쓰면 키와 밸류를 쌍으로 튜플로 보내줌
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4),sep=":") #ljust(확보할 칸수)

# # 은행 대기 순번표
# # 001, 002, 003, ...
# for number in range(1,21):
#     print("대기번호 : " + str(number).zfill(3))#zfill 빈공간 영어로 채워줌

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다." ) #input에서 출력되면 항상 str

# # 다양한 출력포맷
# # 빈 자리는 빈 공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수 일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸은 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기 
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기 
# print("{0:^<+30,}".format(+1000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기 동작, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line) # 파일이 몇줄일지 모를때
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines() # 리스트 형태로 저장
# for line in lines:
#     print(line, end = "")

# score_file.close()

# # pickle 
# import pickle
# # profile_file = open("profile.pickle","wb") # b = binary 피클 쓸땐 항상 정의
# # profile = {"이름" : "박명수", "나이" : 30, "취미":["축구","골프","농구"]}
# # print(profile)
# # pickle.dump(profile,profile_file) #profile에 있는 정보를 profile_file에 저장
# # profile_file.close()
# profile_file = open("profile.pickle","rb") # b = binary 피클 쓸땐 항상 정의
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# # import pickle 

# # with open("profile.pickle","rb") as profile_file:
# #     print(pickle.load(profile_file)) 
# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 -
# 부서 : 
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일 명은 '1주차.txt', '2주차.txt',...와 같이 만듭니다.
# weeks = 1
# contents = {"부서" : ":","이름" : ":","업무 요약" : ":"}
# while True:
#     report_file = open("{}주차.txt".format(weeks),"w",encoding= "utf8") 
#     print("- {} 주차 주간보고 -".format(weeks), file = report_file)
#     for key, value in contents.items():
#         print(key.ljust(0), value.rjust(2), file = report_file)
#     report_file.close()
#     weeks = weeks + 1
#     if weeks > 50:
#         break

# # 나도 코딩 풀이

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고 -\n부서 :\n이름 : \n업무요약 :".format(i))

# # for 가 반복문이라는 사실을 망각하고 어려운 길로 감 _.write는 한가지 문장만 받음
# # 한줄로 구현 할 수 없나? 줄바꿈으로 가능 
# # 파일명을 구현할때 + 를 활용할 수 있음

# # 클래스
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력은 {0}, 공격력{1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력은 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력은 {0}, 공격력{1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
#         name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 클래스 는 붕어빵 틀이다.

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name =name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # __init__ <= 생성자 
# # 클래스로 부터 만들어지는 것은 객체
# # 유닛 클래스의 인스턴스?

# # 멤버변수 => 클래스 내에서 정의된 변수

# # 레이스 : 공중유닛, 비행기. 클로킹 (상대방에게 보이지 않음)

# wraith1 = Unit("레이스", 80 , 5)
# print("유닛이름 :{0}", "공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# # 외부에서 멤버변수 확장가능 그러나 지정해준 객체만 사용가능

# 메소드 

# 일반 유닛

class Unit:
    def __init__(self, name, hp):
        self.name =name
        self.hp = hp
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}".format(self.hp))

# 공격 유닛

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name =name
#         self.hp = hp
#         self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# # 상속

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage


# # 파이어뱃 
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # # 공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)

# # 다중상속

# # 메소드 오버라이딩

# # pass
# # 건물

# class BulidingUnit(Unit) : 
#     def __init__(self, name, hp, location): 
#         pass

# # 서플라이 디폿 : 건물 1개 건물 = 8 유닛.

# supply_depot = BulidingUnit("서플라이 디폿", 500, "7시")

# # pass => class 가 완성된 것처럼 오류 없이 넘길 때 사용

# # super
# class BulidingUnit(Unit) : 
#     def __init__(self, name, hp, location): 
#         Unit.__init__(self, name, hp, 0)
#         self.location = location
# # 일반 적인 상속의 예
# class BulidingUnit(Unit) : 
#     def __init__(self, name, hp, location): 
#         super().__init__(name, hp, 0)
#         self.location = location
# # 다중 상속에선 사용 x

# # Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# # (출력 예제)
# # 총 3대의 매물이 있습니다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년

# # [코드]
# # class House:
#     # # 매물 초기화
#     # def __init__(self, location, house_type, deal_type, price, /
#     # completion_year):
#     #   pass
#     # 
#     # # 매물 정보 표시
#     # def show_detail(self):
#     #   pass
#     #
 
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#         # 매물 정보 표시
#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

# class Logage1(House):
#     def __init__(self):
#         House.__init__(self, "강남", "아파트", "매매", "10억", "2010년")
# class Logage2(House):
#     def __init__(self):
#         super().__init__("마포","오피스텔","전세","5억","2007년")
# class Logage3(House):
#     def __init__(self):
#         super().__init__("송파","빌라","월세","500/50","2000년")


# L1 = Logage1()
# L2 = Logage2()
# L3 = Logage3()

# Logages = []
# Logages.append(L1)
# Logages.append(L2)
# Logages.append(L3)

# print("총 {0}대의 매물이 있습니다.".format(len(Logages)))
# for House in Logages:
#     House.show_detail()

# # 나도 코딩 풀이 
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#         # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


# L1 = House("강남", "아파트", "매매", "10억", "2010년")
# L2 = House("마포","오피스텔","전세","5억","2007년")
# L3 = House("송파","빌라","월세","500/50","2000년")

# Logages = []
# Logages.append(L1)
# Logages.append(L2)
# Logages.append(L3)

# print("총 {0}대의 매물이 있습니다.".format(len(Logages)))
# for House in Logages:
#     House.show_detail()
# # 배웠던걸 다 활용못하는 퀴즈라 아쉬움 종속 클래스를 활용해서 풀이를 했는데
# # 오히려 코드가 복잡해짐

# # 예외처리
# # 에러가 발생했을 때 그걸 처리해줌
# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번쩨 숫자를 입력하세요 : "))
#     num2 = int(input("두번쩨 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫번쩨 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번쩨 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# # 에러 발생시키기
# try: 
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 사용자정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try: 
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:    
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

# # finally 에러가 발생해도 무조건 나옴

# try: 
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:    
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# # Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# # 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# # 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리를 주문하시겠습니까? "))
#     if order > chicken # 남은 치킨보다 주문량이 많을때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#             .format(waiting, order))
#         waiting += 1
#         chicken -= order

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#          return self.msg


# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# try:
#     while(True):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리를 주문하시겠습니까? "))
#         if order <= 0 : 
#             raise ValueError 
#         if chicken <= 0 :
#             raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         if order > chicken : # 남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
# except SoldOutError as err:
#         print(err)
# except ValueError:  
#         print("잘못된 값을 입력하였습니다.")

# # 나도 코딩 풀이

# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

# while(True):
#     try:    
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리를 주문하시겠습니까? "))
#         if order > chicken : # 남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         elif order <= 0 : 
#             raise ValueError 
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:  
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")  
#         break
# # while 구문에 대한 이해부족, 사용자정의 에러를 왜 pass 처리하고 끝내는지 모르겠다.

# 모듈
# 패키지
# pip install
# 내장함수