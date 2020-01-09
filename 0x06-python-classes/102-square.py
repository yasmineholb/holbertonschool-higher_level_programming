#!/usr/bin/python3
Square = __import__('102-square').Square

seq = Square(5)
seqq = Square(6)

if seq < seqq:
    print("Square 5 < Square 6")
if seq != seqq:
    print("Square 5 != Square 6")
if seq <= seqq:
    print("Square 5 <= Square 6")
if seq == seqq:
    print("Square 5 == Square 6")
if seq >= seqq:
    print("Square 5 >= Square 6")
if seq > seqq:
    print("Square 5 > Square 6")
