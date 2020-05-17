import unittest
import regex

class Test(unittest.TestCase):

    #Test the . operator
    def test_dot_operator_true1(self):
        #get the results of the function
        result = regex.match("a.b|b*", "bbb")
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    #Test the . operator
    def test_dot_operator_false1(self):
        #get the results of the function
        result = regex.match("a.b|b*", "bbcb")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

    #Test the . operator
    def test_dot_operator_true2(self):
        #get the results of the function
        result = regex.match("a.b", "ab")
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    def test_dot_operator_false2(self):
        #get the result of the function
        result = regex.match("a.b", "abc")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

    def test_dot_operator_true3(self):
        #get the result of the function
        result = regex.match("b**", "b")
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    def test_dot_operator_false3(self):
        #get the result of the function
        result = regex.match("b**", "abc")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

    def test_dot_operator_true4(self):
        #get the result of the function
        result = regex.match("a|b", "a")
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    def test_dot_operator_false4(self):
        #get the result of the function
        result = regex.match("a|b", "aa")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

    def test_dot_operator_true5(self):
        #get the result of the function
        result = regex.match("ab*", "")
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    def test_dot_operator_false5(self):
        #get the result of the function
        result = regex.match("ab*", "abb")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

#run the tests
unittest.main()


