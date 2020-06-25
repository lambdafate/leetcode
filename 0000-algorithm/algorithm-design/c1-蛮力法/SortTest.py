import unittest
import Sort
from random import randint


class SortTest(unittest.TestCase):

    def assert_sorted_array(self, array):
        for i in range(len(array)-1, 0, -1):
            self.assertTrue(array[i] >= array[i-1])
        return None

    def setUp(self):
        self.tests_array = []
        for _ in range(randint(10, 50)):
            tmp = []
            for t in range(randint(0, 1000)):
                tmp.append(randint(-1000, 1000))
            self.tests_array.append(tmp)

    def tearDown(self):
        self.tests_array = []

    def test_select_sort(self):
        for array in self.tests_array:
            Sort.select_sort(array)
            self.assert_sorted_array(array)

    def test_bubble_sort(self):
        for array in self.tests_array:
            Sort.bubble_sort(array)
            self.assert_sorted_array(array)


if __name__ == "__main__":
    unittest.main()
