import time
import random
import os


# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()


'''
작업 코드 작성
'''


# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")