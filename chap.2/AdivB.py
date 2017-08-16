#Q: A/B를 계산하시오.

#IN: 첫째 줄에 A와 B가 주어진다. (0 < A,B < 10)

#OUT: 첫째 줄에 A/B를 출력한다. 절대/상대 오차는 10-9 까지 허용한다.

a,b = input().split()

a = float(a)
b = float(b)

if a>0:
    if b<10:
        def div(x, y):
            result = x / y
            return result


        temp = div(a, b)

        print(temp)
