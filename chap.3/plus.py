#Q: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

#IN: 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

#OUT: 1부터 n까지 합을 출력한다.

n = int(input())

def plus(x):
    sum=0
    for i in range(0,x+1):
        sum=sum+i
    return sum
if 1<=n<=10000:
    print(plus(n))