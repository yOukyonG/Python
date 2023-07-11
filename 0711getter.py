# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:18:44 2023

@author: USER
"""


class Student:
    def __init__(self, name = "noname"):
        self.__name = name # 속성 이름이 __로 시작하므로 instance로 접근 불가
    # 접근자 메서드
    def getName(self):
        print("name 의 getter 호출")
        return self.__name
    
    def setName(self, name):
        print("name 의 setter 호출")
        self.__name = name
    
    # Property 생성
    # name을 호출하면 getName 메서드가 호출되고, name에 값을 대입하면 setName 메서드가 호출
    name = property(fget=getName, fset=setName)
        
stu = Student()
#setter와 getter 를 직접 호출
stu.setName("공유경") #값 불러오기

#property를 이용한 setter와 getter 호출
stu.name = "홍인혁"
print(stu.name)



#-----
class Student:
    @property #getter 설정
    def name(self):
        print("name 의 getter 호출")
        return self.__name
    
    @name.setter
    def name(self, name):
        print("name 의 setter 호출")
        self.__name = name
    
stu = Student()
#setter와 getter 를 직접 호출
# stu.name("공유경") #값 불러오기


#------ 
class Student:
    def __init__ (self, name ="noname"):
        self.name = name
        
# + 연산자 오버로딩
    def __add__(self, other):
        return self.name + "," + other.name
    
# == 연산자 오버로딩 (내부요소 값 비교)
    def __eq__(self,other):
        return self.name == other.name
        
stu1 = Student("연산자")
stu2 = Student("연산자")
stu3 = stu1
print(stu1+stu2)

print(stu1 == stu2) # 값(내부 요소)을 비교, True
print(stu1 is stu2) # id를 비교, False

#
class Student():
    def __init__ (self, name="noname",count=0):
        self.name = name
        self.count = count
        
    def __add__(self, other):
        return self.count + other.count
    
stu1 = Student("사과",4)
stu2 = Student("오렌지",6)
print(stu1+stu2) #원하는 메서드의 기능을 변경할 수 있음

#----
class Sup:
    def __init__(self):
        self.name = "noname"
        
    def superMethod(self):
        print("상위 클래스의 메서드")
        
# Sup 클래스를 상속받는 Sub 클래스
class Sub(Sup):
    # 하위 클래스에서 __init__ 를 생성하면 상위 클래스의 __init__ 을 호출하지 않움
    # 하위클래스에 __init__를 만들 때믄 상위 클래스의 __init__ 을 호출해주어야 함.
    def __init__(self):
        super().__init__()
        self.score = 80
    def subMethod(self):
        print("하위 클래스의 메서드")

#Sub의 인스턴스 생성해서 필요한 메서드 호출
s = Sub()
s.subMethod() 
s.superMethod() #Sub 클래스에는 없지만 Sup의 상속을 받아 호출가능

print(s.name)
print(s.score)






