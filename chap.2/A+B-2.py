#Q: A+B를 계산하시오.

#IN: 첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)

#OUT: 첫째 줄에 A+B를 출력한다. (A+B < 10)

a = int(input())
b = int(input())

def puls(x,y):
    if a>0:
        if b<10:
            sum = x + y
            return sum

def output():
    temp = puls(a,b)
    if temp<10:
        print(temp)

output()
