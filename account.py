"""
Created on Mon Jan 24 11:30:20 2022

@author: Pappa
"""

class Account:

    user_id = 0
    acc_num = 0
    acc_type = ""
    balance = 0

    def __init__(self, user_id, acc_num, acc_type, balance):
        self.user_id = user_id
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.acc_balance = balance
        
    # represents the class objects as a string
    def __str__(self):        
        return "\nCustomer ID: " + str(self.user_id) + "\nAccount Number: " + str(self.acc_num) + "\nAccount Type: " + self.acc_type + "\nBalance: " + str(self.balance)