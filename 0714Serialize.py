# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 11:21:26 2023

@author: USER
"""

# 읽기 'r'
# 마지막데이터에는 \n이 추가됨
# 마지막 줄에 \n제거하기
import csv
data = []
with open('C:/Users/USER/Downloads/경기도 연천군_반려동물 등록현황_20230713.csv','w', encoding = "CP949") as file:
    # for line in file:
    #     ar = line.split(',')
    #     data.append(ar)
        
    # rdr = csv.reader(file)
    # for line in rdr:
    #     data.append(line)
    
    wr = csv.writer(file)
    wr.writerow(['이름','학번','학과'])

data =[]
with open('./test.bin','wb') as file:
    file.write("안녕하세요".encode())
with open('./test.bin','rb') as file:
    content = file.read()
    print(content.decode())
    
    
    
class DTO:
    def __init__(self, num=0, name = "이름없음"):
        self.__num = num
        self.__name = name
        
    @property
    def num(self):
        return self.__name
    
    @num.setter
    def num(self, num):
        self.__num = num
    @num.setter
    def name(self, name):
        self.__name = name
    #인스턴스를 print함수에 대입했을 때 호출되는 메서드 (오버라이딩)
    #출력을 편리하기위해서 재정의 - 디버깅 목적
    def __str__(self):
        return str(self.__num) + ":" + self.__name

#파일에 기록할 데이터 생성
dto1 = DTO(1,"kong")
dto2 = DTO(2,"hong")

print(dto1)
print(dto2)        
        
import pickle
try:
    with open("./data.dat","rb") as f:
        #f에 저장된 내용을 Deserializable
        result = pickle.load(f)
        for dto in result:
            print(dto)
except Exception as e:
    print(e)
    
    
import zipfile
filelist = ["./data/data.dat","./data/test.dat"]

#파일을 순회하면서 압축
with zipfile.ZipFile("./data/test.zip","w") as myzip:
    for temp in filelist:
        myzip.write(temp)
        
# 압축 해제       
zipfile.ZipFile("./data/test.zip").extractall()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        