"""
Given the names and grades for each student in a class of N students.
Store them in a nested list and print the names(s) of any student(s) having the second lowest grade.

Note :
if there are multiple students with second lowest grade, order their names alphabetically and
print each names on a new line.

Example :
records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
the ordered list of scores are [20.0,50.0], so the second lowest score is 50.0.
There are two students with that score: ['beta','alpha'].
if ordered alphabetically, the names are printed as ,

output:
    alpha
    beta

"""
if __name__ == "__main__":

    nestedList = []
    scoresList = []

    def create_nested(arr):
        nestedList.append(arr)
        scoresList.append(arr[1])

    for _ in range(int(input("N : "))):
        name = input("name : ")
        score = float(input("score: "))

        create_nested([name, score])


    rem_dup = []

    for score in scoresList:
        if score in rem_dup:
            continue
        rem_dup.append(score)

    value = rem_dup[0]
    for i in rem_dup:
        if value > i:
            value = i
        continue

    def findSecondLowestMark(sl, ls):
        sl.sort()
        for i in range(len(sl)):
            if sl[i] == ls:
                print("sl: ",sl[i+1])
                return sl[i+1]

    secondLowestMark = findSecondLowestMark(rem_dup, value)

    def check_grader(nl, slm):
        graders = []
        for i in nl:
            if i[1] == slm:
                graders.append(i)
        return graders

    list_of_second_graders = check_grader(nestedList, secondLowestMark)

    list_of_second_graders.sort()

    for name in list_of_second_graders:
        print(name[0])

