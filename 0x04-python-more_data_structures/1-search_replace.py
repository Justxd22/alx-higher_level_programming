#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    mc = list(my_list)
    for x in mc:
        if x == search:
            mc[mc.index(x)] = replace
    return mc
