#Q: 두 자연수 A와 B가 주어진다. 이 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

#IN: 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

#OUT: 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a,b = input().split()

a = int(a)
b = int(b)
if a>0:
    if b<10001:
        def plus(x, y):
            result = x+y
            return result

        def minus(x, y):
            result = x - y
            return result

        def mul(x, y):
            result = x * y
            return result

        def div(x, y):
            result = x / y
            return result
        def rem(x,y):
            result = x % y
            return result

        numP = plus(a,b)
        numM = minus(a,b)
        numMul = mul(a,b)
        numDiv = int(div(a,b)) # 결과값이 소수점이 생략이 였다.
        numR = rem(a,b)

        print(numP)
        print(numM)
        print(numMul)
        print(numDiv)
        print(numR)