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
