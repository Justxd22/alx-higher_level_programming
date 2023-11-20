#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        r = 0
        try:
            r = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        finally:
            list.append(r)
    return list
