import unittest
import check_bouncy as cb


class TestChecker(unittest.TestCase):

    def test_check_bouncy(self):
        self.assertFalse(cb.check_bouncy(134468))
        self.assertFalse(cb.check_bouncy(66420))
        self.assertTrue(cb.check_bouncy(155349))
        self.assertFalse(cb.check_bouncy(0))

    def test_bouncy_number(self):
        pass


if __name__ == '__main__':
    unittest.main()
