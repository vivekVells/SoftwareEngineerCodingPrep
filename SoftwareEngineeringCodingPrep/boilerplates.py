import unittest

'''
    unit test boilerplate
'''
class TestReverseNumber(unittest.TestCase):
    def setUp(self):
        pass

    def test_(self):
        pass


if __name__ == "__main__":
    unittest.main()

'''
    to have a generic file that can be
    used to identify the questions and 
    proceed accordingly
'''
exercise_info = ""
question_no_start_str = "Question 1 start"
question_no_end_str = "Question 1 end"
current_exercise_info = ""

with open('../exercises.txt', 'r') as file:
    exercise_info = file.readlines()

# print(exercise_info)

is_fill_current_exercise_info = False
for line in exercise_info:

    if question_no_start_str in line:
        is_fill_current_exercise_info = True
    elif question_no_end_str in line:
        is_fill_current_exercise_info = False

    if is_fill_current_exercise_info:
        current_exercise_info += line


with open('reverse_number_exercise_question.txt', 'w+') as file:
    file.write(current_exercise_info)