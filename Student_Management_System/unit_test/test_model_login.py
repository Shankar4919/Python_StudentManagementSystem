import unittest
from model.user_login import *


class Test_login(unittest.TestCase):
    def setUp(self):
        self.stu = login_detail('admin','pass')

    def test_set_user(self):
        self.stu.set_username('admin1')
        self.assertEqual('admin1', self.stu.get_username())

    def test_get_roll(self):
        self.assertEqual('admin', self.stu.get_username())

    def test_set_pass(self):
        self.stu.set_password('shankar')
        self.assertEqual('shankar', self.stu.get_password())

    def test_get_pass(self):
        self.assertEqual('pass', self.stu.get_password())

    def tearDown(self):  # after completion of tast
        self.stu = None


if __name__ == '__main__':
    unittest.main()


