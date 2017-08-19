#Q: 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#IN: 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 자연수이다.

#OUT: 시험 성적을 출력한다.

score = int(input())

def test(x):
    if 100>=x>=90:
        result = "A"
    elif 90> x >= 80:
        result = "B"
    elif 80> x >= 70:
        result = "C"
    elif 70> x >= 60:
        result = "D"
    else: result = "F"

    return result

print(test(score))
