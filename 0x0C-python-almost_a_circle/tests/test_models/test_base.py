#!/usr/bin/python3
"""test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test"""
    def test1(self):
        """test """
        bs = Base(55)
        self.assertEqual(bs.id, 55)

    def test2(self):
        """test"""
        bs = Base()
        self.assertEqual(bs.id, 1)

    def test3(self):
        """test """
        bs = Base("hello")
        self.assertEqual(bs.id, "hello")

    def test4(self):
        """test """
        bs = Base(None)
        self.assertEqual(bs.id, 2)

    def test5(self):
        """test """
        bs = Base({"yass": "hm"})
        self.assertEqual(bs.id, {"yass": "hm"})

    def test6(self):
        """test """
        self.assertTrue(len(Base.__doc__) > 0)
