#Q:(A+B)%C는 (A%C + B%C)%C 와 같을까?
#(A×B)%C는 (A%C × B%C)%C 와 같을까?
#세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.

#IN: 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

#OUT: 첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.

a, b, c = input().split()
3
a = int(a)
b = int(b)
c = int(c)


def rem1(x, y, z):
    temp = (x + y) % z
    return temp
def rem2(x, y, z):
    temp = (x % z + y % z) % z
    return temp
def rem3(x, y, z):
    temp = (x * y) % z
    return temp
def rem4(x, y, z):
    temp = (x % z * y % z) % z
    return temp

def output():
    if a > 1:
        if b < 10001:
            if c < 10001:

                result1 = rem1(a, b, c)
                result2 = rem2(a, b, c)
                result3 = rem3(a, b, c)
                result4 = rem4(a, b, c)

                print(result1)
                print(result2)
                print(result3)
                print(result4)

output()