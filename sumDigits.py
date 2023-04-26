def sum_digits(whole_number):
    number_string = str(whole_number)
    lenth_of_string = len(number_string)
    total = 0
    for i in range(0, lenth_of_string):
        total += int(number_string[i])
    return total


print(sum_digits(int(input(">> "))))