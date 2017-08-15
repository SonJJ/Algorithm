#python은 input이 str형식으로 입력된다.
#그점에 유의해서 형을 지정해주자.
a = int(input('A를 입력하세요(조건: 0 < A) : '))
b = int(input('B를 입력하세요(조건: B < 10) : '))

if a < 1:
    print('조건 불충족, A가 0이하.')
if b > 9:
    print('조건 불충족, B가 10이상.' )
else:
    print('A + B = ', a+b)