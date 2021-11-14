from src.interpolation import LinearInterpolator
from numpy import allclose
import unittest


class LinearInterpolatorTests(unittest.TestCase):
    def setUp(self):
        xs = [1, 2, 3, 4, 5, 6]
        ys = [x ** 2 for x in xs]
        self.interpolator = LinearInterpolator(xs, ys)

    def test_interpolate_point(self):
        res = self.interpolator.interpolate_point(2.6)
        self.assertTrue(allclose(res, 7), msg='point failed')

    def test_array(self):
        xs = [1.2, 2.3, 3.7, 4.5]
        ys = [1.6, 5.5, 13.9, 20.5]
        res = self.interpolator.interpolate_array(xs)
        self.assertTrue(allclose(res, ys), msg='array failed')

    def test_extrapolation(self):
        res = self.interpolator.interpolate_array([-1, 0, 7, 10])
        self.assertTrue(allclose(res, [-5, -2, 47, 80]), msg='array extrapolation failed')
        res = self.interpolator.interpolate_point(8)
        self.assertAlmostEqual(res, 58, msg='point extrapolation failed')
        res = self.interpolator.interpolate_point(-2.2)
        self.assertAlmostEqual(res, (-2.2 - 1) * (4 - 1) + 1, msg='point extrapolation failed')


if __name__ == '__main__':
    unittest.main()
