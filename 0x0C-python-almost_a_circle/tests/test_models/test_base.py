import unittest
from models.base import Base


class BaseModelTestCase(unittest.TestCase):
    def test_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1, b2)

    def test_id_is_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id-1)

    def test_id_not_none(self):
        b3 = Base(7)
        self.assertEqual(7, b3.id)

    def test_instance_after_unique_id(self):
        b1 = Base()
        b2 = Base()
        b4= Base(None)
        self.assertEqual(b4.id-1, b2.id)

if __name__ == '__main__':
    unittest.main()
