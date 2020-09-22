# 입력한 숫자가 짝수면 짝수 홀수면 홀수를 출력함
x = int(input())  # input 사용자에게 입력받음
if (x % 2) == 1:
    print("홀수")
else:
    print("짝수")
    
# 1~10까지 숫자중 홀수만 출력
num = 1  # num은 숫자를 저장하기 위한 변수
for num in range(1, 11):  # num:변수명 in range:1~10까지 숫자를 만듦
    if (num % 2 == 1):
        print(num)

# 입력된 변수의 값의 포맷팅 %d 정수 %s문자 %f실
age = 5
print("i am %d year old" %age)

# list
rainbow=["빨","주","노","초","파","남","보"]
# indexing
print(rainbow[0])
print(rainbow[-2])
# slicing
print(rainbow[2:4])
# 함수
# append 리스트안에 값추가 ["빨", "주", "노", "초", "파", "남", "보", "흰"]
rainbow.append("흰")
# insert 리스트안에 위치에 값추가 ['빨', '주', '노', '검', '초', '파', '남', '보', '흰']
rainbow.insert(3,"흰")
# remove 좌>우로 먼저 만나는 리스트의 값을 삭제
rainbow.remove("흰")
# del 리스트의 index로 값 삭제
del rainbow[0]
# sort a~z순 ㄱ~ㅎ순 정렬 수행
rainbow.sort()
# reverse 이름의 역순 정
rainbow.reverse

a = ['kim',20]
b = ['park',40]
c = a+b # ['kim', 20, 'park', 40]
d = a*3 # ['kim', 20, 'kim', 20, 'kim', 20]

# tuple
lee = ('lee',40,20,30)
shin = ('shin', 30, 40, 60)

# dictionary {key:value}
person = {'name':'kim', 'location':'seoul'}
# dictionary 값의 변경
person['name'] = 'shin'
# dictionary 값의 추가
person['birthday'] = "4/12"
# dictionary 값의 삭제
del person['name']

# set
age = {10,20,30,10}
print(age) # {10, 20, 30}

#**
num = 10
num ** 2 # num의 2

