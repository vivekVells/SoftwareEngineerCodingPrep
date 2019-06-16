# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(current_pos, dest_pos, fixed_hop):
    hop_count = 1
    jump_pos_now = 0

    if current_pos == dest_pos: return 0

    while True:
        if jump_pos_now >= dest_pos:
            hop_count -=1
            break
        elif jump_pos_now < dest_pos:
            jump_pos_now = current_pos + (fixed_hop * hop_count)
            hop_count += 1

    return hop_count


print(solution(10, 100, 10))