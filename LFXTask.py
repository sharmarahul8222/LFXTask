import unittest
def print_list(list):
    #Create empty list to store filtered element
    filtered_list=[]

    #Condition to check if list is multiple of 10 or not.
    if len(list) % 10 != 0:
        raise ValueError("Invalid!!! The input list must be a multiple of 10 in length.")
    
    #Condition to check if list is empty or not.
    elif len(list) == 0:
        raise ValueError("Invalid!!! List should not be empty.")
    
    else: 
        #Loop to remove elements that are not at position which are multiple of 2 and 3.
        for i in range(len(list)):
            if(i+1) % 2 != 0 and (i+1) % 3 !=0:
                filtered_list.append(list[i])
        print("Output List: ", filtered_list)
        return filtered_list
    
#Test Cases   
class testList(unittest.TestCase):
    #Test Case: For expected output
    def test_list(self):
        list=[1,2,3,4,5,6,7,8,9,10]
        expected_output=[1,5,7]
        self.assertEqual(print_list(list), expected_output)

    #Test Case: For invalid length
    def test_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            print_list([1,2,3,4,5])
        self.assertEqual(str(context.exception), "Invalid!!! The input list must be a multiple of 10 in length.")

    #Test Case: For empty list
    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            print_list([])
        self.assertEqual(str(context.exception), "Invalid!!! List should not be empty.")

if __name__ == '__main__':
    unittest.main()