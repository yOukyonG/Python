# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:01:56 2023

@author: USER
"""
#1번
count = 0
count2 =0
with open('C:/Users/USER/Downloads/log.txt','r',encoding="UTF-8") as file:
    for idx in file:
        # print(idx)
        #읽어낸 한 줄을 공백을 기준으로 list로 생성
        data = idx.split()
        # print(data)
        if data[8] =='200':
            count += 1
        if data[-1] == "-":
            count2 +=1
print(count2)


# #----------------
# #2번 ip별 접속 횟수 - 첫번째 항목이 ip
# #Dict 생성
ipCount = {}
from collections import Counter
with open('C:/Users/USER/Downloads/log.txt','r',encoding="UTF-8") as file:
    for idx in file:
        data = idx.split()
        #data[0] -> ip값
        #data[0] 을 key로 해서 1더하기
        #기존의 값을 가져오는데 없으면 0
        ipCount[data[0]] = ipCount.get(data[0],0) + 1
for ip in ipCount:
    print(ip, ipCount[ip])
    

# #3번 ip별 트래픽 합계
# - ->0 으로 바꾸기
trCount = {}
with open('C:/Users/USER/Downloads/log.txt','r',encoding="UTF-8") as file:
    for idx in file:
        data = idx.split()
        try:
            trCount[data[0]] = trCount.get((data[0]),0) + int(data[-1])
        except Exception as e:
            print(e)    
for ip in trCount:
    print(ip, ":" , trCount[ip])
print(data)






