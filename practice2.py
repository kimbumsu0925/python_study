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

