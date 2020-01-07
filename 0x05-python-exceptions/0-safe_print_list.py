#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    m = 0
    try:
        for i, m in zip(my_list, [0, x]):
            print("{:d}".format(m))
    except:
        print("hell")
