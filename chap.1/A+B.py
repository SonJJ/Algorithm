#2.
#A: 두 수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#In: 첫째 줄에 A와 B가 주어진다. (0 < A,B < 10) (ex: 1 2)
#out: 첫째 줄에 A+B를 출력한다. (ex: 3)

#python은 input이 str형식으로 입력된다.
#그점에 유의해서 형을 지정해주자.

# a, b = int(input().split())
#위에 형태로 사용하지 않는 이유는
# split()메소드가 str 형태에 입력값을 처리할떄 사용되기 때문이다.
a, b = input().split()

#a, b를 문자 형태로 입력받아 처리후 정수형태로 자료변환을 해줘야 에러가 나지않음.
a = int(a)
b = int(b)

if a > 0:
    if b < 11:
        result = a + b
        print(result)