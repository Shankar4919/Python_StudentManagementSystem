import unittest
from front_end.student_management import manage_student


class test_search(unittest.TestCase):
    def setUp(self):
        v1=[4,'Krisha','Female','2000/01/01','computing','123@123','9090992309','Nepal','Dhading','Smajong']
        v2=[10,'Aagya','Female','2000/12/12','Civil Engeneering','me@aagya','990921','Nepal','KTM','Dhumbaharai']
        v3=[14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara']
        self.value=[v1,v2,v3]

    def test_search_algorithm(self):
        search_value='Aagya'
        index=1
        expect = [[10,'Aagya','Female','2000/12/12','Civil Engeneering','me@aagya','990921','Nepal','KTM','Dhumbaharai']]
        actual = manage_student.linear_search(self.value,search_value,index)
        self.assertEqual(actual,expect)

    def test_search1(self):
        search_value1='Meena'
        index2=1
        expect1=[[14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara']]
        actual1=manage_student.linear_search(self.value,search_value1,index2)
        self.assertEqual(actual1,expect1)

    def tearDown(self):
        self.value=None


if __name__ == '__main__':
    unittest.main()

