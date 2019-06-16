# binary gap length find


def solution(num):
    num_str = str(num)
    current_bin_gap_len = 0
    max_bin_gap_len = 0

    for val in num_str[1:]:
        if val != '1':
           current_bin_gap_len += 1
        elif val == '1':
            if current_bin_gap_len > max_bin_gap_len:
                max_bin_gap_len = current_bin_gap_len
                current_bin_gap_len = 0

        print("current_bin_gap_len: ", current_bin_gap_len, "max_bin_gap_len: ", max_bin_gap_len)

    return max_bin_gap_len


print(solution(1110100011100001))
# for num in range(483647):
#     print(solution(num))