#Q: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

#IN: 첫째 줄에 N (1<=N<=100)이 주어진다.

#OUT: 첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.

n = int(input())

def star(x):
    if 1<=x<=100:
        for i in range(0,n):
            dot = "*"
            temp = dot*(i+1)
            print(temp)
star(n)