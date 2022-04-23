import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 5)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)

    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',6,3), 5) # will call the mock

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_DividByZerrorEx1(self):
        with self.assertRaises(ValueError):
             calculate('4','3','w')
    
    ##OR

    def test_DividByZerrorEx2(self):
        self.assertRaises(ValueError, calculate, '4','3','w') 

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')

    
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1',3,2)
        self.assertEqual(result, 4)


    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,6), 5)
        


    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9)

    def test_AddInvalid(self):
        self.assertEqual(add(2,4), 5)
        self.assertEqual(calculate('1',2,4), 5)

    def test_SubPass(self):
        self.assertEqual(subtract(4,2), 2)
        self.assertEqual(calculate('2',4,2), 2)

    def test_SubInvalid(self):
        self.assertEqual(subtract(5,2), 2)
        self.assertEqual(calculate('2',5,2), 2)

        ## in calclate function ... the implement of multiply fun is not correct >> the result fail  
        ##بضرب مرتين  
        ## to correct >>delete "  num1, "*", num2, "="  " in line 67
    def test_MultiplyValid(self):
        self.assertEqual(multiply(4,2), 8)
        self.assertEqual(calculate('3',4,2), 8)

    def test_MultiplyInvalid(self):
        self.assertEqual(multiply(2,1), 3)
        self.assertEqual(calculate('3',2,1), 3)

    def test_DivideValid(self):
        self.assertEqual(divide(6,2), 3)
        self.assertEqual(calculate('4',6,2), 3) 

    def test_DivideInvalid(self):
        self.assertEqual(divide(6,2), 2)
        self.assertEqual(calculate('4',6,2), 2) 

    def test_DivideByZero(self):
        self.assertEqual(divide(11,0), 0)
        self.assertEqual(calculate('4',11,0), 0) 

    def test_DividePass(self):
        self.assertEqual(divide(0,5), 0)
        self.assertEqual(calculate('4',0,5), 0) 

    def test_check_user_inputValid(self):
        self.assertEqual(check_user_input("7"))

    def test_check_user_inputInvalid(self):
        self.assertEqual(check_user_input(" "))

    def test_check_user_inputInvalid(self):
        self.assertEqual(check_user_input("o"))

    def test_isExitValid(self):
        self.assertEqual(isExit("no"))

    def test_isExitInvalid(self):
        self.assertEqual(isExit("ok"))

    def test_isExitValid(self):
        self.assertEqual(isExit("yes"))

    def test_CalcluteError(self):
        self.assertEqual(calculate('2', 5, ),2)

    #def test_CalcluteError(self):
      #  self.assertEqual(calculate('2', ,5),2)

    def test_CalcluteError(self):
        self.assertEqual(calculate('5',1 ,2),2)
    


if __name__ == '__main__':
	unittest.main()