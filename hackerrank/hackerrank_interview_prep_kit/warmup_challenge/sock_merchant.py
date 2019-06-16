"""
Input Format

The first line contains an integer
, the number of socks represented in .
The second line contains space-separated integers describing the colors

of the socks in the pile.

Constraints

where

Output Format

Print the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3

find the pairs of colors thats it.
"""

from itertools import groupby

def sockMerchant(n, ar):
    ar.sort()
    pair_count = 0

    freq = { key : len(list(group)) for key, group in groupby(ar)}

    for value in freq.values():
        pair_count += value // 2



    # if n <= 1: return 0
    #
    # for i in range(0, n, 2):
    #     if ar[i] == ar[n-1]:
    #         pass
    #     elif ar[i] == ar[i+1]:
    #         pair_count +=1

    return pair_count


print(sockMerchant(9, [10,20,20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(9, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3] ))

"""
Output:
3
"""