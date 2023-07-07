# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:03:18 2023

# @author: USER
# """
# FUNCTION 

def display(text, num) -> None:
    for i in range(num):  
        print(text)
        
display("Hello Python",2)
display("Hello Java",3)

print("hi"*3)

help(sorted)

def intAddint (a,b):
    return a+b

result = intAddint(100,300)
print(intAddint(100,300),600)
# 함수의 수행이 종료되기 전에 다른 함수를 호출하여
# 2개의 스택이 동시에 존재하는 경우가 발생

def intOpwithInt(a,b):
    return a+b, a-b
#튜플로 만들어서 return

t= intOpwithInt(100,200)
print(t) #(300,-100) 튜플형태

add, sub = intOpwithInt(100, 200)
print(add, sub) #300 -100 튜플 분해해서 받기

def add(a: int, b:int) -> int:
    return a+b

def callbyvalue(a: int) -> None:
    a = 20
    print(a)
    
K=13
callbyvalue(K) #20 , K가 아닌 값 30을 전달함
print(K) #13

def callByReference(li: list) -> None:
    li[0] = 20 
    print(li)
    
l =[100,200,300]
callByReference(l) #[20, 200, 300]
print(l) #[20, 200, 300]

def collect(a,b):
    print(a, end=" ")
    print(b)
# collect(10,20)

#   # dic는 *이 하나이면, key 값이 매개변수에 전달됨
collect(*[100,200]) # list를 분할해서 a와 b에 대입/ 100 200
collect(*{"key1":100, "key2":200}) #key1 key2

# dic는 **이면, value값이 매개변수에 전달됨
#이때, key 이름과 매개변수 이름이 같아야함
collect(**{"a":100, "b":200}) #100 200



def merge(*li):
    for element in li:
        print(element, end=" ")
merge(10)
merge(10,20)
merge(10,20,30)

def merge(*li, name):
    for element in li:
        print(element)
# merge(name ="kong", 10,20,30)
# merge(name = "kong", 10, 20, 30) # 에러 발생
# merge(10,20,30,"kong") # 에러 발생, 가변 매개변수 뒤의 데이터는 이름과 함께 호출 필요!
merge(10,20,30, name="kong")



def merge (name, **param):
    for k in param:
        print(k, param[k])

merge(name ="adam", job="singer", gender="남자")




