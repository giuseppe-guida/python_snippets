import unittest
from unittest import TestCase
from ut_stage0 import Solver

class Init_TestSolver(TestCase):
   def setUp(self):
      self.s = Solver()

class TestSolver(Init_TestSolver):
   def test_foo_zero_division_exc(self):
      self.assertRaises(Exception, self.s.foo, 2.0, 0)

   def test_foo_correct(self):
      self.assertEqual(self.s.foo(4.0,2.0), 2.0, 'incorrect division')

   def tearDown(self):
      self.s = None

if __name__ == '__main__':
    unittest.main()