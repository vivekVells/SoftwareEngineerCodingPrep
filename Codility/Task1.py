"""
loop through from A to B
with initial_val as 1, on each loop
    check whether initial_val ^ 2 vs item in range[A,B] inclusive
        initial_val should be reinitalized everytime in a loop and squared vs item
make number of counts


"""


def solution(A, B):

    count_val = 0

    for item in range(A, B + 1):
        initial_val = 1;

        while True:
            squared_initial_val = initial_val * initial_val

            if squared_initial_val <= item:
                if squared_initial_val == item:
                    count_val = count_val + 1
                initial_val = initial_val + 1
            else:
                break

        #item = item + 1

    return count_val

print(solution(4,9))