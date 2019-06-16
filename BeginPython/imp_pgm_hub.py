# find max key, max value in a given dictionary
d= {'a': 7, 'b': 3}
max_key = ''
max_value = 0

for i in d.keys():
    if d[i] > max_value:
        max_value = d[i]
    if i > max_key:
        max_key = i

print(d, max_key, max_value)
# {'a': 7, 'b': 3} b 7

# count frequency:
#    refer frequency.py