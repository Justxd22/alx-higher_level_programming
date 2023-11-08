#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    z = []
    sum = 0
    for x in my_list:
        if x not in z:
            sum += x
            z.append(x)
    return sum
