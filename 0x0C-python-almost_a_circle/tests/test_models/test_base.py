import unittest
from models.base import Base


class BaseModelTestCase(unittest.TestCase):
    def test_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1, b2)

    def test_id_not_none(self):
        b3 = Base(7)
        self.assertEqual(7, b3.id)

if __name__ == '__main__':
    unittest.main()
