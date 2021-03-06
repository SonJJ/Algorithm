#Q: 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
#  설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#  상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때,
#  3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#  상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

#IN: 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

#OUT: 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

n = int(input())

def rem(x):
    if 3 <= x <= 5000:
        five = 0
        temp = 1    #초기화를 잘하자
        resultB = x
        while (five*5) <= x: #5kg 갯수*5가 설탕 무게를 넘지못함
            sugar = x
            sugar = sugar-(five*5)

            three = sugar//3 #3kg 갯수
            div = sugar%3  # 나머지

            resultA = five + three
            five = five + 1  # 5kg 갯수를 하나씩 증가

            if div == 0:
                if resultA < resultB : # B(전), A(후) A가 B보다 갯수가 적으면 변경
                    resultB = resultA
                    temp = 0   # 정확한 결과값 존재 유무 판독용

        if temp == 0:  #결과값 존재 유무
            result = resultB
        else:
            result = -1

    return  result

def output():
    index = rem(n)
    print(index)

output()

