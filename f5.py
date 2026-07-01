def min_max(royxat):
    if len(royxat)==0:
        return 0
    
    max = royxat[0]
    min = royxat[0]

    for i in royxat:
        if i>max:
            max = i
        if i<min:
            min = i

    return max,min

print(min_max([5, 2, 9, 1, 7]))