# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:28:06 2023

@author: USER
"""
# 쓰기 'w'
import os
# print(os.getcwd()) #상대경로 설정할 때 기준경로
try:
    file = open('./0714.test.txt','w', encoding = "UTF-8")
    file.write("문자열") #문자열 기록
    lines = ["Tigers","Eagles","SSG","\n"]
    lines2 = ['기아타이거즈','한화이글스', '쓱',"\n"]
    file.writelines(lines)
    file.writelines(lines2)
except Exception as e:
    print("파일 처리 중 예외 발생",e)
finally:
    file.close()
    
    
# 읽기 'r'
with open('./0714.test.txt','r', encoding = "UTF-8") as file:
    for line in file:
        print(line)
        print()
    # content = file.read() #전체 읽기
    # print(content)
    