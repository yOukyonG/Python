# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:14:41 2023

@author: USER
"""
#클래스 생성
class Student:
    # 생성자 = 인스턴스를 생성할 때 호출하는 메서드
    # 이 메서드에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어 주는 것이 좋음
    # 매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화가 가능
    # 매개변수를 이용해서 초기화할 때 매개변수에 기본값을 설정하지 않으면,
    # 인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야함.
    
    def __init__ (self, name="noname"):
        print("인스턴스 생성")
        self.name = name 
        # self.name = "기본값" # 특정한 상수로 생성하고자 하는 경우, 내부에서 직접 설정
    # 소멸자 : 인스턴스가 소멸될 때 호출되는 메서드
    def __del__(self):
        print("인스턴스 소멸")
        
        
        
        
    #클래스에 만들어지지만, 인스턴스 없이는 호출 불가한 메서드
    def disp(self):
        print("Instance Method")
        
    #setter : 속성을 수정하거나 생성하는 메서드
    def setName(self, name):
        self.name = name # name이라는 속성이 없으면 만들어서 대입하고 존재하면 수정
    
    #getter : 속성의 값을 사용할 수 있도록 return 하는 메서드
    def getName(self):
        return self.name

stu1 = Student() #인스턴스 생성   
Student.disp(stu1)
stu1.disp()



#메서드 호출 : Class 안에 만들어진 기능 (함수)
Student.disp(stu1) #클래스가 인스턴스의 메서드를 호출 (Unbound 호출)
stu1.disp() #self에 인스턴스가 대입돼서 메서드를 호출 (Bound 호출)

# stu1.setName("Kong")
print(stu1.getName())



# ----
