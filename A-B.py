#3.
#직전 문제와 동일
a = int(input('A를 입력하세요(조건: 0 < A) : '))
b = int(input('B를 입력하세요(조건: B < 10) : '))

if a < 1:
    print('조건 불충족, A가 0이하.')
if b > 9:
    print('조건 불충족, B가 10이상.' )
else:
    print('A - B = ', a-b)