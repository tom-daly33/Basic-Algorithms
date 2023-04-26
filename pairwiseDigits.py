def make_up_difference_in_length(str_needed, difference):
    for i in range(1, difference + 1):  # adds on reqiured extra digits
            str_needed = str_needed + "-"
    print(str_needed)
    return (str_needed)



def pairwise_digits(number_a, number_b):
    number_a = str(number_a)
    number_b = str(number_b) # converts both ints to strs

    difference = len(number_a) - len(number_b) # finds difference in lengths
    if (difference > 0):
        number_b = make_up_difference_in_length(number_b, difference)

    elif (difference < 0):
        number_a = make_up_difference_in_length(number_a, abs(difference))

    length = len(number_a)

    print(number_a, number_b)
    req_output = ""
    for j in range(0, length):
        if number_a[j] == number_b[j]:
            req_output = req_output + "1"
        else:
            req_output = req_output + "0"
    
    return(req_output)


print(pairwise_digits(int(input("1st number >> ")), int(input("2nd number >> "))))


        



