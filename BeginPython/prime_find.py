for number in range(2, 10):
    for num in range(2, number):
        if number % num == 0:
            print(number, 'equals', num, '*', number/num)
            break
        else:
            print(number, 'is a prime number')
            break


# for n in range(2, 10):
#     print("n: ", n)
#     for x in range(2, n):
#         print("x: " , x)
#         if n % x == 0:
#             print(n, 'equals', x, '*', n/x)
#             break