# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:20:37 2023

@author: USER
"""

class Student:
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    #클래스 속성과 생성자를 이용한 일련번호
    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment      
        
    def __del__(self): #소멸자
        print("Instance 소멸")
    
    
stu1 = Student() #인스턴스가 생성되고 참조 카운트가 1이 됨
stu1 = None  # 참조를 가리키는 변수에 None을 대입하면 참조 카운트가 1 감소
             # 참조 카운트가 0이면 인스턴스가 소멸됨
print("프로그램 종료")
stu2 = Student() #참조 카운트 1
stu3 = stu2 #다른 변수에 참조를 대입하므로 참조 카운트는 1 증가 -> 2
stu2 = None #참조 카운트가 1 줄어들어도 1 -> 인스턴스가 소멸되지 얺움
print("프로그램 종료")

# print(stu1.no)
# stu2 = Student()
# print(stu2.no)

#--------------

class Student:
  
    # @staticmethod
    # def method():
    #     print("매개변수가 없는 static method")
        
    def __init__(self):
        self.name = "kong"
        self.__no = 1 # 속성을 만들 때__로 시작하면 인스턴스는 속성에 접근
        
# Student.method() 
stu1 = Student() 
print(stu1.name)
print(stu1.__no)      

#----------------

class Student: #
    #na,e 과 age 속성만 사용하도록 제한
    __slots__ = [i]
stu1 = Student()
stu1.name = "kong"
stu1.age = 24
stu1.job = "student" #jo


