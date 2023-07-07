# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:33:33 2023

@author: USER
"""

def hap(n:int) -> int:
    if n == 1:
        return 1
    return n + hap(n-1)
print(hap(100))
print(hap(1000))


#  n번째 피보나치 수열구하기 (재귀함수 이용-> 시간많이 소요됨)
# 첫번째와 두번째는 1, 이후는 이전 2개 항의 합

def fibonacci(n:int) -> int:
    if n ==1 or n==2:
        return 1
    else: 
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(10))

fibonacci.__doc__ = "재귀를 이용해서 피보나치 수열의 값을 return 하는 함수"
help(fibonacci)

# list 배열 이용
# n = int(input("입력하고자하는 수: "))
# result = []
# for idx in range(1,n+1):
#     if idx == 1 or idx==2:
#         res = 1
#         result.append(res)
#     elif idx >=3:
#         res = result[idx-2]+result[idx-3]
#         result.append(res)
# print(res)     

# #재귀함수 없이 구현
# n = int(input("입력하고자하는 수: "))
# res2 = 0
# if n ==1 or n ==2:
#     print(1)
# else:
#     n1 =1 
#     n2 =1
#     for i in range(3,n+1):
#         res2 = n1 + n2
#         n2= n1
#         n1 = res2
#     print(res2)

# 함수의 매개변수에 설명추가 가능

    
    
