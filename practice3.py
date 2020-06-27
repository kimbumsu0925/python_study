# # array
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.zeros((2,3))
# arr3 = np.arange(10)
# arr4 = np. random.randint(1,45,6)
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)

# sub = arr3[0]
# print(sub)
# sub2 = arr3[0:3]
# print(sub2)
# sub3 = arr3[arr3 < 5]
# print(sub3)

# print(len(arr3[arr3%2 == 1]))
# count = 0
# for i in range(len(arr3)):
#     if arr3[i] % 2 == 1:
#         count += 1
# print(count) 

# i = 0
# count = 0
# while i < len(arr3):
#     if arr3[i] % 2 == 1:
#         count += 1
#     i += 1
# print(count) 

# # function
# arr1 = np.array([1,2,3])
# arr2 = np.array([0,4,4])
# print(arr1)
# print(arr2)

def odd(arr): 
    n = len(arr[arr % 2 ==1])
    return n
# a*x**2 + b*x + c = 0 (a!=0)
def determinent(a,b,c):
    if a != 0:
        D = b**2 - 4*a*c
        if D > 0:
            print("서로 다른 두 실근")
        elif D == 0:
            print("서로 같은 두 실근")
        else:
            print("서로 다른 두 허근")
    else:
        print("이차 방정식이 아닙니다.")

# determinent(2,3,4)

