def sum_lists(list_2D):

    output = []

    for row in list_2D:
        total = 0
        for val in row:
            total += val
        output.append(total)

    return(output)

