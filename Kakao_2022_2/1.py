#9개 입력 받기
def getHobit(hobit):
    for i in range(9):
        hobit.append(int(input()))

#진짜 7개 출력하기
def printReal(hobit):
    for i in hobit:
        print(i)

#9개 중 진짜 7개 찾기
def findReal(hobit):
    for i in range(len(hobit)):
        for j in range(i+1, len(hobit)):
            if (sum(hobit) - (hobit[i]+hobit[j])) == 100:
                hobit.remove(hobit[i])
                hobit.remove(hobit[j-1])
                printReal(hobit)
                break
hobit = []
getHobit(hobit)
findReal(hobit)