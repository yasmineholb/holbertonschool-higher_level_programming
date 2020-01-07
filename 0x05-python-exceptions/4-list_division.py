#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    s = 0
    try:
        for i, j in zip(my_list_1, my_list_2):
            s = i / j
            new.append(s)
        print("{}".format(new))
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by zero")
    except IndexError:
        print("out of range")
    finally:
        print("{}".format(new))
        
