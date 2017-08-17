#Q: N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

#IN: 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

#OUT: 입력으로 주어진 숫자 N개의 합을 출력한다.

n = input()
num = input()

def plus(n, num):
    n= int(n)
    sum=0
    if num[n-1]==num[-1]:   #갯수 초과 확인
        for i in range(0,n):
            if num[i]!="":
                sum= int(num[i])+sum
            else:
                break
    return sum
print(plus(n, num))
