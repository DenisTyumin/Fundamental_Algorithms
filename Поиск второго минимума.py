array = [1, 1, 3, 4]
min = array[0]
min_2 = array[1]
for i in array:
    if i < min:
        min_2 = min
        min = i   
    elif  i < min_2 and i > min and min != min_2:
        min_2 = i
print(min, min_2)