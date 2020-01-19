#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestStringMethods(unittest.TestCase):
    """
    this is the add function
    """
    def test_integer1(self):
        self.assertEqual(max_integer([1, 2, 5, 8]), 8)

    def test_integer2(self):
        self.assertEqual(max_integer([-1, -9, -1000, 0]), 0)

    def test_element(self):
        self.assertEqual(max_integer([1]), 1)
        
    def test_string(self):
        self.assertEqual(max_integer(['hh', 'hhh', 'hhhh']), 'hhhh')

    def test_empty(self):
        self.assertEqual(max_integer(), None)
            
    def test_empty1(self):
        self.assertEqual(max_integer([]), None)
