# # -*- coding: utf-8 -*-
# """
# Created on Tue Jul 11 14:06:35 2023

# @author: USER
# """

# class Sup:
#     def Method(self):
#         print("상위 클래스의 메서드")
        
# # Sup 클래스를 상속받는 Sub 클래스
# class Sub(Sup):
#     #상위 클래스에 존재하는 메서드를 하위 클래스에서 다시 정의 (Overriding)
#     #목적은 기능 확장
#     def Method(self):
#         super().method() #상위 클래스의 메서드 호출
#         print("하위 클래스의 메서드")

# #Sub의 인스턴스 생성해서 필요한 메서드 호출
# s = Sub()
# s.Method() 

# #-----------
# import abc
# # 추상클래스 - 자신의 인스턴스 생성 불가
# class AbstractClass(metaclass = abc.ABCMeta):
# #추상메서드 - 내용이 없는 메서드로 하위클래스에서 구현해서 사용해야함
#         @abc.abstractmethod 
#         def method(self):
#             pass
# class Sub(AbstractClass):
#     def __init__(self):
#         print("인스턴스 생성")
        
#         #추상클래스를 상속받는 경우, 추상 메서드를 반드시 implementation 해줘야 함
#         # 그렇지 않으면 에러 발생
        
#     def method(self):
#         print("추상메서드 구현")
# instance = Sub()
    

# #추상 클래스는 인스턴스를 만들 수 없어 에러
# # instance = AbstractClass()


#---------------
# import sys
# print(sys.modules)
# print(sys.path)

# import mymath
# sys.path.append("./") #현재 디렉토리에서 모듈이나 패키지를 검색하도록 설정
# print(mymath.MYPI)
# mymath.func("모듈사용")



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,7))
plt.boxplot(([100,87,29,43,24],[23,44,13,1000,39]))
plt.grid()
plt.show()
fig.savefig("graph.png")

from decimal import Decimal
print(((Decimal('0.223')+Decimal('9.2'))+Decimal('3.5')))
print((Decimal('0.223')+(Decimal('9.2')+Decimal('3.5'))))


print(Decimal('0.2')==Decimal('1.0')-Decimal('0.8'))



import random as rd
import time

rd.sample(range(1000),6)

li = ["ssg","hanwha","samsung","LG Twins"]
for i in range(10):
    print(li[rd.randint(0,len(li)-1)])

# help(rd.shuffle)

# arr = [1,2,3,4,5]
# rd.shuffle()

import random as rd
i = input("정수 6자리를 공백으로 구분해서 작성해주세요 : ")
i = i.split(" ")
print(i)
lotto = list(map(lambda e : int(e), i))
lotto.sort()
print(lotto)


#1부터 45 까지 숫자에서 6개를 랜덤 추출해서 몇 번 만에 일치하는 지 확인
ar = range(1,46)
cnt = 0
while True:   
   k = rd.sample(ar,6)
   k.sort()
   cnt += 1
   if lotto == k:
       print("로또 당첨 !")
       break;    
print(cnt,"번을 시도하였습니다.")



#-- 
x = input("2자리 숫자를 입력하세요: ")
arr2 = range(10, 100)
cnt = 0
while True:
    k = rd.sample(arr2,1)
    if arr2 == k:
        print("일치합니다.")
        break;
        

    




















