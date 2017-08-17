#Q: 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

#IN: 첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

#OUT: 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

x, y = input().split()
x = int(x)
y = int(y)

def cal(mon, day):
    sum = 0
    for i in range(1,mon+1):
        if i<9 : #8월을 기준으로 31일 30일 변경됨
            if i == 1:  #1월은 전월 누적일수 없음
                sum = 0
            elif i ==3: #3월은 2월이 28일만 누적됨
                sum = sum+28
            elif i%2 == 0:  #짝수달은 전원일 홀수달(31일)이다.
                sum = sum+31
            else:
                sum = sum+30
        else:
            if i%2 ==0: #8월을 기준으로 31일 30일 변경됨
                sum = sum+30
            else:
                sum = sum+31
    sum=sum+day
    week = sum%7    #일주일은 7일 나머지값에 따른 요일

    if week==1: result="MON"
    elif week==2: result="TUE"
    elif week==3: result="WED"
    elif week==4: result="THU"
    elif week==5: result="FRI"
    elif week==6: result="SAT"
    else: result="SUN"

    return result
if 1<=x<=12 and 1<=y<=31:
    print(cal(x,y))

