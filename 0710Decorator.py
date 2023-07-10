# # -*- coding: utf-8 -*-
# """
# Created on Mon Jul 10 14:01:16 2023

# @author: USER
# # """
# def decorator(func):
#     print("새로운 업무 프로세스")
#     func()
    
# # # 이제 부터 businesslogic 이라는 함수를 호출하면 decorator 함수 수행
# # # deco에게 매개변수로 businessLogic 이라는 함수가 전달됨
# # # 개발자가 작성한 코드 대신 다른 코드를 불러내는 방식을 프록시 패턴이라고 함.
# @decorator
# def businessLogic():
#     print("업무로직")
    
# businessLogic()
    
# # 고객의 니즈가 변경
# # 업무 로직과는 관계가 없는 로깅을 출력하는 코드를 추가하기를 원하는 방향으로 변경
# # 유지보수 관정이나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우
# # 업무 로직을 직접 수정하는 것은 예상치 못한 결과 만들어낼 수 있음
# # 이런 경우에는 업무 로직은 손을 대지 않고 가능하도록 만드는 것이 좋음!

# def deco(func):
#     func()
#     print("로깅")

# @deco
# def businessLogic():
#     print("업무로직")
# businessLogic()

# import time 
# def clock(func):
#     #decorator가 적용된 함수가 호출되면 수행될 실제 함수
#     def clocked(*args):
#         start = time.time() #현재 시간을 기록
#         result = func(*args)  #업무 조직 함수를 호출
#         end = time.time()
#         elapsed = end - start #함수의 수행시간
#         print("수행시간:", elapsed)
        
#         #매개변수 확인
#         print("매개변수:", args)
#         print("리턴값 : ",result)
#         return result
#     return clocked

# import functools
# @functools.lru_cache()

# @clock
# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
        
# print(fibonacci(10))


# # Method
# class Student:
# # 인스턴스가 있어야만 호출되는 메서드
#     def disp(self):
#         print("Instance생성")
#     def setName(self, name):
#         self.name = name #self.name은 인스턴스의 속성으로 만들어짐 *self가 빠지면 지역변수

# # 인스턴스 생성
# stu = Student()
# stu.setName("학생")
# print(stu.name)

# stu.score = 100 #인스턴스에 score 속성이 있으면 수정, 없으면 생성됨
# print(stu.score)

# # # 메서드 호출 - Bound 호출
# # student.disp()

# # # 메서드 호출 - Unbound 호출
# # Student.disp(student)
# # Student.disp(Student())


# class Student:
#     class_data = "클래스 속성"
    
# student = Student()
# print(Student.class_data) #클래스 이름을 이용해서 클래스 속성 접근 //클래스 속성
# print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성 접근 //클래스 속성


# Student.class_data = "클래스 이름으로 데이터 수정"
# print(Student.class_data) #클래스 이름 이용// "클래스 데이터 수정"
# print(student.class_data) #인스턴스 이름 이용해서 클래스 속성에 접근 //"클래스 데이터 수정"

# # 인스턴스 student 에 class_data가 없기에 새로 생성
# student.class_data = "인스턴스 이름으로 데이터 수정"
# print(Student.class_data) # "클래스 데이터 수정"
# print(student.class_data) # "클래스 데이터 수정2"

# # instance는 메서드를 가지고 있지않음
# class Student:
#     def method(self):
#         print(self.data)
# student = Student()
# student.data = "Hi"
# student.method() # "Hi"
# # Student.method() # 오류 발생

# Student.method(student) #"Hi" self.data 대신 student.data가 입력되기에 student.data 결과 출력

# class Student:
#     class_data = "클래스의 속성"

# #인스턴스 생성해서 대입
# stu1 = Student()
# stu2 = Student()
# # stu1 의 데이터 대입 : stu1 이 참조하고 있는 데이터의 참조를 stu3가 참조
# stu3 = stu1

# #2개의 인스턴스가 동일한지 여부를 확인
# print(stu1 == stu2) # 내부 데이터가 같은 지 확인 // False
# print(stu1 == stu3) # //True
# print(stu1 is stu3) # id가 같은지 확인 // True


# 이름과 점수를 갖는 객체를 여러 개 필요
class Student:
    def getName(self):
        return self.name
    
    def setName(self, name):
        return self.name = name
        
    def getName(self):
        return self.name
    
    def setScore(self,score):
        return self.score = score
        
stu1 = Student()
#setter를 이용한 속성 생성과 설정
stu1.setName("kong")
stu1.setScore(98)
    
#getter를 이용한 속성 사용
print(stu1.getName())
print(stu1.getScore())
#최근에 등장한 IDE는 대부분 getter와 setter를 만드는 유틸 제공

















