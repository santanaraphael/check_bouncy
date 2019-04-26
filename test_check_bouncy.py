import unittest
import check_bouncy as cb


class TestChecker(unittest.TestCase):

    def test_check_bouncy(self):
        self.assertFalse(cb.check_bouncy(134468))
        self.assertFalse(cb.check_bouncy(66420))
        self.assertTrue(cb.check_bouncy(155349))
        self.assertFalse(cb.check_bouncy(0))

    def test_bouncy_number(self):
        self.assertEqual(cb.bouncy_number(538), 538*0.5)
        self.assertEqual(cb.bouncy_number(21780), 21780*0.9)


if __name__ == '__main__':
    unittest.main()
