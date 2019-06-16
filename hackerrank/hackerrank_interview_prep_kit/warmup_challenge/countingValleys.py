def countingValleys(n, s):
    UP_HILL = 'U'
    DOWN_HILL = 'D'
    valley_count = 0
    height = 0
    prev_height = 0


    for direction in s:
        # if direction == UP_HILL:
        #     height += 1
        # elif direction == DOWN_HILL:
        #     height -= 1

        height += 1 if direction == UP_HILL else -1 if direction == DOWN_HILL else 0

        if height == 0 and prev_height <0:
            valley_count += 1
        prev_height = height

    return valley_count


print(countingValleys(8, "UDDDUDUU"))