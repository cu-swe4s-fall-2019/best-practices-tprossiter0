import unittest
import random
import get_column_stats as stat


class TestCalc(unittest.TestCase):
    def test_mean_positive(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(i)

        self.assertEqual(stat.calculate_mean(testvec),  50)

    def test_mean_negative(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(-i)

        self.assertEqual(stat.calculate_mean(testvec),  -50)

    def test_mean_zero(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(i-50)

        self.assertEqual(stat.calculate_mean(testvec),  0)

    def test_mean_random(self):
        testvec = []
        for i in range(0, 1001):
            testvec.append(random.randint(1, 100))

        self.assertIsNotNone(stat.calculate_mean(testvec))

    def test_stdev_positive(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(1)

        self.assertEqual(stat.calculate_stdev(testvec),  0)

    def test_stdev_negative(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(-1)

        self.assertEqual(stat.calculate_stdev(testvec),  0)

    def test_stdev_zero(self):
        testvec = []
        for i in range(0, 101):
            testvec.append(0)

        self.assertEqual(stat.calculate_stdev(testvec),  0)

    def test_stdev_random(self):
        testvec = []
        for i in range(0, 1001):
            testvec.append(random.randint(1, 100))

        self.assertIsNotNone(stat.calculate_stdev(testvec))

    def test_exceptions_mean(self):
        testvec = []
        with self.assertRaises(Exception):
            stat.calculate_mean(testvec)

    def test_exceptions_stdev1(self):
        testvec = []
        with self.assertRaises(Exception):
            stat.calculate_stdev(testvec)

    def test_stdev_1element(self):
        testvec = [0]
        self.assertEqual(stat.calculate_stdev(testvec), "stdev of n=1 set is meaningless")
