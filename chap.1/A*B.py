#Q: 두 정수 A와 B를 입력받은 다음, A*B를 출력하는 프로그램을 작성하시오.

#IN: 첫째 줄에 A와 B가 주어진다. (0 < A,B < 10)

#OUT: 첫째 줄에 A*B를 출력한다.


a, b = input().split()
a = int(a)
b = int(b)

def multi(x,y):
    temp = x * y
    return temp

if a>0:
    if b<11:
        result = multi(a,b)
        print(result)

