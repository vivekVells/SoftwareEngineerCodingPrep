"""
Write a function called sortReindeer (sort_reindeer in Ruby) that accepts an array of Reindeer names, and returns an array with the Reindeer names sorted by their last names.
Example
sort_reindeer([
  "Dasher Tonoyan",
  "Dancer Moore",
  "Prancer Chua",
  "Vixen Hall",
  "Comet Karavani",
  "Cupid Foroutan",
   "Donder Jonker",
   "Blitzen Claus"
])
Returns =>
[
  "Prancer Chua",
  "Blitzen Claus",
  "Cupid Foroutan",
  "Vixen Hall",
  "Donder Jonker",
  "Comet Karavani",
  "Dancer Moore",
  "Dasher Tonoyan",
]
"""

def sort_reindeer(unsorted_arg_lst):
    print(unsorted_arg_lst)
    result = [unsorted_arg_lst[0]]

    for name in unsorted_arg_lst[1:]:
        pass

    pass

print(sort_reindeer(["Vivek Vellaiyappan", "Sharan VivekVai", "Shalini VaiVivek"]))