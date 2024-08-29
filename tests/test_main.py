import unittest
from src.main import add, subtract


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 0), 1)
        self.assertEqual(subtract(2, 2), 0)


if __name__ == "__main__":
    unittest.main()
