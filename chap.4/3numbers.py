#Q: 세 정수 A, B, C가 주어진다. 이 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

#IN: 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

#OUT: 두 번째로 큰 정수를 출력한다.

a, b, c =input().split()
a = int(a)
b = int(b)
c = int(c)

def sort(a,b,c):
    if b>a:
        temp = a
        a = b
        b = temp
    if c>b:
        temp = b
        b = c
        c = temp
        if b>a:
            temp = a
            a = b
            b = temp
    result = b
    return result

print(sort(a,b,c))