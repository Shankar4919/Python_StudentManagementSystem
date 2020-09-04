import unittest
from model.student2 import *


class Test_Student(unittest.TestCase):
    def setUp(self):
        self.stu=student2(1,'Mamba','Male','1999/20/20','Python','hello@','123456789','Nepal','KTM','Boudha')
        self.stu2 = student2(5, 'Shankar', 'Male', '1999/20/21', 'Newtworking', 'hello@11', '123456789', 'Nepal',
                             'KTM', 'Boudha')

    def test_set_roll(self):
        self.stu.set_roll(4)
        self.assertEqual(4,self.stu.get_roll())

    def test_get_roll(self):
        self.assertEqual(1,self.stu.get_roll())

    def test_set_contact(self):
        self.stu.set_contact('98132223')
        self.assertEqual('98132223',self.stu.get_contact())

    def test_get_contact(self):
        self.assertEqual('123456789',self.stu.get_contact())

    def test_get_name(self):
        self.assertEqual('Mamba',self.stu.get_name())
        self.assertEqual('Shankar',self.stu2.get_name())

    def tearDown(self):  # after completion of tast
        self.stu=None
        self.stu2=None


if __name__=='__main__':
    unittest.main()
