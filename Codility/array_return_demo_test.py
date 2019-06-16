"""
This is a demo task.
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
""" 
got 55 points

def solution(A):
    if len(A) < 2:
        if A[0] <= 0:
            return 1
        else:
            return 2 if A[0] == 1 else 1

    A = [item for item in A if item >= 0]

    if len(A) == 0: return 1

    A = set(A)
    min_positive = 1

    for item in A:
        if min_positive < item:
            return min_positive
        else:
            min_positive += 1

    return min_positive
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()

    min_positive = 0
    negative_count = 0

    if len(A) < 2:
        if A[0] <= 0:
            return min_positive
        else:
            return 2 if A[0] == 1 else min_positive

    for item in A:
        if item < 0:
            negative_count += 1
        else:
            if min_positive < item:
                min_positive +=1

    if len(A) == negative_count: return 1
    else: return 2 if min_positive == 1 else min_positive

# print(solution([3, 6, 4, 2 ]))

i = 97
print(['  ' + chr(i)  for i in range(97,123,1)])
print([i for i in range(97,123,1)])


