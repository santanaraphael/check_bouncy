import unittest
import check_bouncy as cb


class TestBouncyNumbers(unittest.TestCase):

    def test_check_bouncy(self):
        self.assertFalse(cb.check_bouncy(134468))
        self.assertFalse(cb.check_bouncy(66420))
        self.assertTrue(cb.check_bouncy(155349))
        self.assertFalse(cb.check_bouncy(0))

    def test_bouncy_number(self):
        self.assertEqual(cb.bouncy_number(538), 538*0.5)
        self.assertEqual(cb.bouncy_number(21780), 21780*0.9)

    def test_bad_args(self):
        self.assertRaises(TypeError, cb.check_bouncy, 323.23)
        self.assertRaises(TypeError, cb.bouncy_number, 323.23)
        self.assertRaises(TypeError, cb.check_bouncy, 'hollywood')
        self.assertRaises(TypeError, cb.bouncy_number, 'coffee')
        self.assertRaises(TypeError, cb.challenge, 'foo')
        self.assertRaises(ValueError, cb.challenge, 1)

if __name__ == '__main__':
    unittest.main()
