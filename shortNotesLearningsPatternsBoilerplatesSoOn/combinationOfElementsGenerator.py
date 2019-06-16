# wrd = "abcd"
# cmbn_wrds = [wrd]
#
# for i in range(len(wrd) - 1):
#     wrd = wrd[1:] + wrd[0]
#     cmbn_wrds.append(wrd)
#
# print("Given Word: {}\nPossible combination of given words: {}".format(wrd, cmbn_wrds))
# print(cmbn_wrds)

# https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python

from itertools import permutations

print(([''.join(p) for p in permutations('121')]))
print((set([''.join(p) for p in permutations('121')])))

"""
Output:
C:\Developer\Python36\python.exe E:/kevDev/PythonDev/shortNotesLearningsPatternsBoilerplatesSoOn/combinationOfElementsGenerator.py
['121', '112', '211', '211', '112', '121']
{'112', '211', '121'}
"""