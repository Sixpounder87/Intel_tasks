import math
import unittest

from intel_task_3.merge import merge


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.generator_1 = (x * x * 2 for x in range(1, 20, 2))
        self.generator_2 = (x for x in range(3, 51, 5))
        self.generator_3 = (math.factorial(x) for x in range(2, 10))

    def test_merge_one_arg(self):
        expected_out = [2, 18, 50, 98, 162, 242, 338, 450, 578, 722]
        res = merge(self.generator_1)

        actual_out = []
        for i in res:
            actual_out.append(i)
        self.assertEqual(expected_out, actual_out)

    def test_merge_two_args(self):
        expected_out = [2, 3, 8, 13, 18, 18, 23, 28, 33, 38, 43, 48, 50, 98, 162, 242, 338, 450, 578, 722]
        res = merge(self.generator_1, self.generator_2)

        actual_out = []
        for i in res:
            actual_out.append(i)
        self.assertEqual(expected_out, actual_out)

    def test_merge_three_args(self):
        expected_out = [2, 2, 3, 6, 8, 13, 18, 18, 23, 24, 28, 33, 38, 43, 48, 50, 98, 120, 162, 242, 338, 450, 578,
                        720, 722, 5040, 40320, 362880]
        res = merge(self.generator_1, self.generator_2, self.generator_3)

        actual_out = []
        for i in res:
            actual_out.append(i)
        self.assertEqual(expected_out, actual_out)


if __name__ == "__main__":
    unittest.main()
