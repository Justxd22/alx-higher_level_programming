import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test.

    Attributes:
        pass
    """

    def test_init(self):
        r = Rectangle(10, 20, 5, 7, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_str(self):
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 1, 8)
        expected = {'id': 8, 'width': 5, 'height': 10, 'x': 2, 'y': 1}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
