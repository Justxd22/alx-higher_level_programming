import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test.

    Attributes:
        pass
    """

    def test_create_instance(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_create_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1, 'x': 2, 'y': 3}]),
                         '[{"id": 1, "x": 2, "y": 3}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1, "x": 2, "y": 3}]'),
                         [{'id': 1, 'x': 2, 'y': 3}])


if __name__ == '__main__':
    unittest.main()
