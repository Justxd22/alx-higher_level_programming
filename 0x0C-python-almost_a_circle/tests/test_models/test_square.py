import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test.

    Attributes:
        pass
    """

    def test_init(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_str(self):
        s = Square(3, 1, 4, 7)
        self.assertEqual(str(s), "[Square] (7) 1/4 - 3")

    def test_update(self):
        s = Square(2, 1, 1, 1)
        s.update(3, 4, 5, 6)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_to_dictionary(self):
        s = Square(4, 2, 2, 8)
        expected = {'id': 8, 'size': 4, 'x': 2, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_csv_row(self):
        s = Square(3, 2, 1, 5)
        expected = [5, 3, 2, 1]
        self.assertEqual(s.to_csv_row(), expected)


if __name__ == '__main__':
    unittest.main()
