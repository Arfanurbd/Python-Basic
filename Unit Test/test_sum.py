import unittest

class uniTest(unittest.TestCase):


#Test Case
    def test_sum_tc1(self):
        assert sum([1, 1,]) == 2, "should be 2"

    def test_sum_tc2(self):
        assert sum([1, 1, 1]) == 3, "should be 3"

    def test_sum_tc3(self):
        assert sum([1, 1, 1,1, 1]) == 5, "should be 5"


    def test_sum_tc3(self):
        assert sum([2, 3, 4, 5]) == 14, "should be 14"
