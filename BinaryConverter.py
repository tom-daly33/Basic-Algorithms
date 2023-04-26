
amount_divided= 0
number = int(input(">>> "))

binary_string = ""

while (number > 0):
    if (number % 2 == 1):
        binary_string = ("1" + binary_string)
    elif (number % 2 == 0):
        binary_string = ("0" + binary_string)
    number //= 2

print (binary_string)