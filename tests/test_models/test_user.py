#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Test Suite for User class"""

    def setUp(self):
        """ Before any test """
        usr = User()
        usr.email = "test@gmail.com"
        usr.password = "password"
        usr.first_name = "first_name"
        usr.last_name = "last_name"
        self.u = usr
        

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.u, User)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()