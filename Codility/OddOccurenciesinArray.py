def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result


print(solution([1,3,5,3, 2, 1]) )