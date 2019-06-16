st = "aba"
st10 = (st * 10)[:10]

count_dict = {}
count = 0
max_letter = ""
max_letter_count = 0

for letter in st10:
    if letter in count_dict:
        count_dict[letter] += 1
    else:
        count_dict[letter] = 1

    if count_dict[letter] > max_letter_count:
        max_letter = letter

print(count_dict, max_letter, max(count_dict.values()))


def get_max_letter(sn):
    count_dict = {}

    for letter in sn:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

    # return max(count_dict.keys(), key=lambda x: count_dict[x])
    # return max((value, key) for key, value in count_dict.items())[1]
    return max(count_dict.items(), key = lambda x: x[1])



# Complete the repeatedString function below.
def repeatedString(s, n):
    sn = (s * n)[:n]
    print("repeatedStr: ", get_max_letter(sn))

if __name__ == "__main__":
    repeatedString(st, 10)

"""
{'a': 7, 'b': 3} a 7
repeatedStr:  ('a', 7)
"""