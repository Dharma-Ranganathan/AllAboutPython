"""
Given the participant's score sheet for your university sports day.
you are required to find the runner_up score.
you are given n scores. store them in a list and find the score of runner_up.

Input format:
the first line contains n. the second line contains an array A[] of n integers
each separated by a space.

Output format:
print the runner_up score.

sample input :
5
2 3 6 6 5

sample output :
5

Explanation :
Given list [2,3,6,6,5]. the maximum score is 6. second maximum is 5,
hence we print 5 as the runner-up score.
"""
if __name__ == "__main__":
    n = int(input("n : "))
    arr = list(map(int, input("score : ").split()))

    arr.sort()
    # print(arr)
    rem_dup = []
    for score in arr:
        if score in rem_dup:
            continue
        rem_dup.append(score)

    # last_before_element
    print(rem_dup[-2:][0])







