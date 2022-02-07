"""
Created on Mon Jan 24 11:30:20 2022

@author: Pappa
"""

class Account:
    
    '''
    From: https://realpython.com/python3-object-oriented-programming/
    class attributes are attributes that have the same value for all class instances.
    A class attribute is defined by assigning a value to a variable name outside of .__init__().
    '''

    user_id = 0
    acc_num = 0
    acc_type = ""
    acc_balance = 0

    def __init__(self, user_id, acc_num, acc_type, acc_balance):
        
        '''
        Instance Attributes:
        Attributes created in .__init__() are called instance attributes.
        An instance attribute’s value is specific to a particular instance of the class.
        All Account objects have a user_id, an acc_num, an acc_type and a balance,
        but the values for the these attributes will vary depending on the Account instance
        '''
        
        self.user_id = user_id
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.acc_balance = acc_balance
        
        '''
        __str__() methos is dunder method and it returns a string containing useful information about an instance of the class in a way that when
        print(instance of the class) is used, instead of getting info that the this particular instance is an
        "Account" object at the memory address for example 0x00aeff70, a string representation of the instance is printed.
        '''

    def __str__(self):        
        return "\nCustomer ID: " + str(self.user_id) + "\nAccount Number: " + str(self.acc_num) + "\nAccount Type: " + self.acc_type + "\nBalance: " + str(self.acc_balance)
