# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

# # 점수에 따른 성적
# # score = int(input("점수를 입력하세요 : "))
# # #예외처리 필요
# # print(type(score)) #int형으로 변경
# # if score >=0 and score <= 59:
# #     print("F")
# # elif score <=69:
# #     print("D")
# # elif score <=79:
# #     print("C")
# # elif score <=89:
# #     print("B")
# # elif score <=100:
# #     print("A")
# # else: 
# #     print("에러 발생")
    
# # print("프로그램 종료")
# print(dir(__builtins__))
# #요일 출력 : <dict> 이용해서 구현
# switcher = {
#     0 : "sun",
#     1 : "mon",
#     2 : "tue",
#     3 : "wed",
#     4 : "thru",
#     5: "fri",
#     6: "sat"}
# # dict에서 ger은 일치하는 키가 있으면 그 값을 가져오고
# # 없으면 두번째 매개변수 값을 리턴
# print(switcher.get(7, "알 수 없는 요일"))


# x = 11
# y = False if x<10 else True
# print(x,y)
# # y는 기본적으로 False를 가지고 x가 10보다 크면 True 대입

# age = 25
# status = "성인" if age>20 else "미성년자"
# print(age,status)


# idx = 0
# while idx < 10:
#     print(idx)
#     idx = idx+1
# # 반복문이 모두 수행하고 종료된 경우에 호출
# # break를 만나거나 예외가 발생하면 수행하지 않음
# else:
#     print("반복문 종료")
# print(idx)  #idx = 10


# print(dir(dict()))

# string ="Hello"
# ar = [10,20]
# row = (100,200)
# s = {1000,2000}
# dic = {"key1" : "Value"}


# idx = [9, 16, 31]                                                                           
# for idx in range(1,32,15):
#     print("https://www.donga.com/news/search!p=", idx, sep=""
#           )
# for i in range(3):
#     a= "https://www.donga.com/news/search!p="+ str((i*15)+1)
#     print(a)
    
# #별찍기
# for i in range(1,26):
#     print("*", end = "")
#     if i% 5 ==0: #5개마다 줄바꿈
#         print()

# '''
# i   j = 1*i
# 0 * 0-0
# 1 ** 0-1
# 2 *** 0-2
# 3 **** 0-3
# 4 ***** 0-4

# i   j = 2*i
# 0 * 0-0
# 1 *** 0-3
# 2 ***** 0-5
# 3 ****** 0-7
# 4 ******** 0-9
# '''
# print("1번")    
# for i in range(5):
#     for j in range(i+1):
#         print("*", end='')
#     print()
    

# print("2번")    
# for i in range(5):
#     for j in range(5-i):
#         print("*", end='')
#     print()


# '''
# *
# **
# ***
# **
# *
# '''
# print("3번")
# for i in range(5):
#     if i < 3:
#         for j in range(i+1):
#             print("*", end='')
#     else:
#         for j in range(5-i):
#             print("*", end='')
#     print()

# '''
#       *
#     *   *
#    *     *
#   *       *
#  ***********
#  '''

print("4번")
cnt = 0
for i in range(5):
    cnt = cnt+1
    if i ==0 or i==4:
        for j in range(i+1):
            print(" "*(4-i), end ="")
            print("*", end ="")
        cnt = cnt +1
    else:
        for j in range(5-i):
            print("a", end='')
        for j in range(i):
            print("*", end="")
        cnt = cnt + 1
    print()
    
    for

if *

else 공백*공백

# #완전수 구하기
# cnt = 0
# for num in range(2, 1001):
#     # 합계를 구할 때 무조건 0으로 초기화 하진 X
#     # 약수의 합을 저장할 변수
#     hap = 1
#     #나머지가 0이 나오는 숫자가 약수
#     for su in range(2, num//2 +1):
#         if num % su == 0:
#             hap = hap + su
#     if num == hap:
#         cnt = cnt+1
# print("완전 수의 개수는", cnt)
           











