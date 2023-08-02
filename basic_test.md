import antigravity

file = open('test.txt', 'w')
file.write('sibal')
file.close()

file = open('test.txt')
content = file.read()
print(content)
file.close()

import ramdom
char = "sibal"
print(random.choice(chars))

import time
print(time.time())
print(str(time.time())[-3:])

# encoding

- euc-kr
- euc-jp/shift-jis
- utf-8

# 파이썬에서 한글, 일본어가 깨지는 경우

- py 내부에 맨 처음부분(소스코드의 최상단)에 하기의 내용 작성
- #-\*-coding:euc-kr
- #-\*-coding:utf8
- 참고로 windows 자체의 한글 코드는: cp650001 (유니코드)

# 밴드의 template.py 파일 참고

```
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
```

```
import os
os.mkdir('testfolder')
os.listdir('testfolder') -> 현재경로를 기준으로 하는 상대경로
os.listdir('/Users/gimdaun/Desktop/jong_automation/code/testfolder') -> 절대경로인 경우
```

```
mylist = ['a', 'b', 'c', 'd']
mylist[0]
mylist[3]
mylist[-1]
mylist[-5] -> 인덱스 범위를 넘음
mylist[4] -> 인덱스 범위를 넘음
mylist[1:3] -> 인덱스 1에서 3-1까지

len(mylist)
```
