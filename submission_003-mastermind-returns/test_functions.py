import unittest
from io import StringIO
import sys
from test_base import captured_io
from unittest.mock import patch
from test_base import run_unittests
import mastermind

class TestFunctions(unittest.TestCase):
    def test_create_code(self):
        output = StringIO()
        sys.stdout = output
        for item in range(101):
            self.assertTrue(mastermind.create_code(),True)
        sys.stdout = sys.__stdout__

    def test_correctness(self):
        output = StringIO()
        sys.stdout = output
        self.assertEqual(mastermind.check_correctness(4,5),True)
        self.assertEqual(mastermind.check_correctness(5,7),False)
        sys.stdout = sys.__stdout__

    @patch("sys.stdin", StringIO("123\n3421\n"))
    def test_get_answer_input(self):
        output = StringIO()
        sys.stdout = output
        result = mastermind.get_answer_input()
        # self.assertEqual(result, "1234")
        self.assertEqual(result, "3421")
        sys.stdout = sys.__stdout__

    @patch("sys.stdin", StringIO("1234\n1342\n"))
    def test_take_turns(self):
        output = StringIO()
        sys.stdout = output
        sys.stdout = sys.__stdout__
        answer = ["1","2","3","4"]
        code = [1,2,3,4]
        result = mastermind.take_turn(answer,code)
        compare_tuple = (4,0)
        self.assertEqual(result,compare_tuple)




        




if __name__ == "__main__":
    unittest.main()
