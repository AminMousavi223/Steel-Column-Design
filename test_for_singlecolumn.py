import unittest
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_for(self):
        j = 0
        for i in range(3, 27):
            FS = 1
            j +=1

        self.assertEqual(j, 24)


if __name__ == '__main__':
    unittest.main()
