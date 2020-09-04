import unittest                     # build-in unit testing module
from back_end.back_end import *


class test_dbConnection(unittest.TestCase):
    def setUp(self):
        self.con=Connection()

    def test_insert(self):
        query='insert into student_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(11,'shankar','male','2000','python','mamba@moh','010203203','Nep','Ktm','Boudha')
        self.con.insert(query,values)
        expect=[(11,'shankar','male','2000','python','mamba@moh','010203203','Nep','Ktm','Boudha')]

        query1='select * from student_management where roll=%s'

        val=(11,)
        actual=self.con.user_login(query1,val)
        self.assertEqual(expect,actual)

    def test_update(self):
        query = 'UPDATE student_management set name=%s,gender=%s, dob=%s,class=%s,email=%s,' \
                'contact=%s,country=%s,city=%s, address=%s WHERE roll=%s'
        values = ('Saitama', 'male', '1995/04/03','python', 'samtha@gmail.com', '9843456825', 'nep', 'ktm',
            'jpt',11)
        self.con.update(query, values)
        expect = [
            (11,'Saitama', 'male', '1995/04/03', 'python', 'samtha@gmail.com', '9843456825', 'nep', 'ktm',
             'jpt')]
        actual = self.con.select('SELECT * from student_management WHERE roll=11')
        self.assertEqual(expect, actual)

    def test_delete(self):
        query = 'delete from student_management  WHERE roll=%s'
        values = (11,)
        self.con.delete(query, values)
        expect = []
        actual = self.con.select('SELECT * from student_management WHERE roll=30')
        self.assertEqual(expect, actual)

    def tearDown(self):  # after completion of tast
        self.con=None


if __name__=='__main__':
    unittest.main()

