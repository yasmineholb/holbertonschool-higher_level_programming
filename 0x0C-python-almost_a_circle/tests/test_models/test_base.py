#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

     def test1(self):
          bs = Base(55)
          self.assertEqual(bs.id, 55)

     def test2(self):
          bs = Base()
          self.assertEqual(bs.id, 1)

     def test3(self):
          bs = Base("hello")
          self.assertEqual(bs.id, "hello")

     def test4(self):
          bs = Base(None)
          self.assertEqual(bs.id, 1)

     def test5(self):
          bs = Base({"yass": "hm"})
          self.assertEqual(bs.id, {"yass": "hm"})

     def test6(self):
          self.assertTrue(len(Base.__doc__) > 0)

     
