#!/usr/bin/python3
import sys
if len(sys.argv)-1 == 0:
    print("0 arguments.")
elif len(sys.argv)-1 == 1:
    print("1 argument:\n{}: {}".format(len(sys.argv)-1, sys.argv[1]))
else:
    print("{} arguments:\n{}".format(len(sys.argv)-1, str(sys.argv)),)
    for arg in sys.argv:    
        print("
