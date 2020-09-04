import unittest
from front_end.student_management import manage_student


class test_sort(unittest.TestCase):
    def setUp(self):
        self.v1=[4,'Krisha','Female','2000/01/01','computing','123@123','9090992309','Nepal','Dhading','Smajong']
        self.v2=[10,'Aagya','Female','2000/12/12','Civil Engeneering','me@aagya','990921','Nepal','KTM','Dhumbaharai']
        self.v3=[14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara']
        self.value=[self.v1,self.v2,self.v3]

    def test_sort_desc(self):
        expect = [[14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara'],
                  [10,'Aagya','Female','2000/12/12','Civil Engeneering','me@aagya','990921','Nepal','KTM','Dhumbaharai'],
                  [4,'Krisha','Female','2000/01/01','computing','123@123','9090992309','Nepal','Dhading','Smajong']]
        actual = manage_student.mergeSort(self.value, False)
        self.assertEqual(actual,expect)

    def test_sort_asc(self):
        expect1=[[4,'Krisha','Female','2000/01/01','computing','123@123','9090992309','Nepal','Dhading','Smajong'],
                 [10,'Aagya','Female','2000/12/12','Civil Engeneering','me@aagya','990921','Nepal','KTM','Dhumbaharai'],
                 [14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara']]
        actual1=manage_student.mergeSort(self.value,True)
        self.assertEqual(actual1,expect1)

    def tearDown(self):
        self.value=None


if __name__ == '__main__':
    unittest.main()
