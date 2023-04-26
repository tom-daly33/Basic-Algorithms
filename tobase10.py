def to_base10(binary):
    total = 0
    length = len(binary)
    for i in range(0, length):
        if binary[length - 1 - i] == "1":
            total += pow(2, i)
    return(total)
