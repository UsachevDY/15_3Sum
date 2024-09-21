import unittest

from source.main import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [-1,0,1,2,-1,-4]
        target = 0

        expected = [[-1,-1,2],[-1,0,1]]

        solution = Solution()
        result = solution.threeSum(nums)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_2(self):
        nums = [0,1,1]
        target = 0

        expected = []

        solution = Solution()
        result = solution.threeSum(nums)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_3(self):
        nums = [0,0,0]
        target = 0

        expected = [[0,0,0]]

        solution = Solution()
        result = solution.threeSum(nums)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

