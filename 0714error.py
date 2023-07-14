# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:03:02 2023

@author: KONG
"""
try:
    ar = [10,20,30]
    su = int(input("나눌 수를 입력하세요: "))
    
    i = 0
    j = len(ar) #함수 호출이 여러번 수행하지 않아도 되어 효율적
    while i <j:
        if su == 1:
        #강제로 에러 발생시키기
            raise ValueError("강제 예외 발생")
        # Asserion su값이 2이면 에러메시지가 출력되고, 프로그램 중단됨
        assert su != 2, "su는 2가 입력될 수 없습니다."
        print(ar[i]/su)
        i = i+1
except ValueError as e:
    print("잘못된 값을 입력하였습니다.")
    print(e)
except ZeroDivisionError as e:
    print("0을 입력하였습니다.")
    print(e)
else:
    print("예외 발생하지 않음 !!")
finally:
    print("예외처리 종료")


