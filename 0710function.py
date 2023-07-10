# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:49:30 2023

@author: USER
"""

#1) 반복문을 이용한 변환
#숫자 list를 가지고 제곱한 list를 생성
li = [i for i in range(1000)] #0부터 999까지 리스트 생성
temp = []

for x in li:
    temp.append(x*x)
    
print(temp)

#2) map을 이용한 변환 map(함수, 리스트)
def f(x):
    return x*x

#li의 모든 요소에 f 함수를 적용해서 변환한 결과를 temp에 대입
temp = list(map(f, li)) #map을 이용한 변환 map(함수, 리스트)
print(temp)

temp = list(map(lambda x : x*x, li)) #함수가 한 줄일 경우, lambda를 이용


#3) 3글자 이상인 경우, ...으로 표시
arr = ["hello","name","height","weight"]
def f(x):
    if len(x) >= 3:
        return x[0:3] + "..."
    return x

temp = list(map(f, arr))
print(temp)


# 4) Filter
ar2 = ["김구","안중근","윤봉길",None]
#결측치 여부 확인
print(None in ar2)

def f1(x):
    return x != None

ar = list(filter(f1,ar2))
ar = list(filter(lambda x: x != None,ar2))


#이름이 3자 이상인 데이터만 추출
def f(x):
    return len(x) >= 3
        
result = list(filter(f,ar))

#lambda로 변경
result = list(filter(lambda x: len(x) >=3, ar))
print(result)

# "ㄱ"으로 시작하는 배열 추출하기
result2 = list(filter(lambda x: x[0] >= "가" and x[0] <"나", ar))
print(result2)


#5) 데이터가 컬렉션에 포함되어있는지 확인 : in(반대가 not in)
data = ["1","2","3"]
kwlist = ["2"]

# ar에서 kwlist에  것은 제외하고 list생성
data2 = list(filter(lambda x : x not in kwlist, data))
print(data2)
            
# ar에서 kwlist에 있는 것은 제외하고 list생성
data2 = list(filter(lambda x : x in kwlist, data))
print(data2)
            
# 단어의 포함
# index >0 
key = ["초등학교","중학교","고등학교"]
value = ["elementary","middle school","high school"] 
print(list(zip(key, value))) #[('초등학교', 'elementary'), ('중학교', 'middle school'), ('고등학교', 'high school')]
print(dict(zip(key, value))) #{'초등학교': 'elementary', '중학교': 'middle school', '고등학교': 'high school'}
            
            
#
def outer():
    outer_data = "외부 함수의 데이터"
    def inner():            
        inner_data = "내부 함수 데이터" 
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)
    inner() #내부에서 외부 함수의 데이터 변경
    print(outer_data) 
outer() # 외부 함수의 데이터

# 6)
print("Nonlocal 변수")
def outer():
    outer_data = "외부 함수의 데이터"
    def inner():            
        inner_data = "내부 함수 데이터" 
        # 함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해 이름을 다시 등록
        nonlocal outer_data
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)
    inner() #내부에서 외부 함수의 데이터 변경
    print(outer_data) 
outer() #내부에서 외부 함수의 데이터 변경


print("Global 함수")
outer_data = "전역에 만든 데이터"
def outer():
    outer_data = "외부 함수의 데이터"
    def inner():            
        # 함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해 이름을 다시 등록
        global outer_data
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)
    inner() #내부에서 외부 함수의 데이터 변경
    print(outer_data) 
outer() #외부 함수의 데이터
print(outer_data)


# Closure _함수 외부에서 내부 데이터를 변경하고자 하는 경우
def outer():
    data = 0
    # 자신을 감싸고 있는 함수의 데이터를 수정하는 함수
    def inner():
        nonlocal data
        data = data + 1
        print(data)
    #함수 내부의 데이터를 수정하는 함수를 return 하는 함수 => "Closure"
    return inner
   
closure = outer() #함수를 호출해서 return 하는 함수를 변수에 저장
closure() #1
closure() #2









