import unittest


def rev_num(num):
    is_negative = False

    if num == 0 or num%10 == num:
        return num
    elif num < 0:
        is_negative = True
        num = abs(num)

    result = 0

    while(num != 0):
        last_digit = num%10
        num = num // 10
        result = result * 10 + last_digit

    return result if not is_negative else -result

    # while num != 0:
    #     digit = num % 10
    #     num = num // 10
    #     print(num/10)
    #     result = result * 10 + digit
    #     # print(result)
    # # print(result)
    # return result

# test_case_inputs = [456, -25, 0, 44, -777]
#
# for i in test_case_inputs:
#     print("reverse of {}: {}".format(i, rev_num(i)))

print("\n\n")
# for i in range(0, 30):
#     print(i, "/10: {}".format(i/10))
#     print(i, "//10: {}".format(i//10))
#     print()


class TestReverseNumber(unittest.TestCase):

    def setUp(self):
        self.test_case_inputs = [456, -25, 0, 44, -777]
        self.test_case_output = [654, -52, 0, 44, -777]

    def test_reverse_number(self):
        for idx in range(len(self.test_case_inputs)):
            assert rev_num(self.test_case_inputs[idx]) == self.test_case_output[idx]
            # self.assertEqual(
            #     rev_num(self.test_case_inputs[idx]),
            #     self.test_case_output,
            #     "test cases failed"
            # )


if __name__ == "__main__":
    unittest.main()