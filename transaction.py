"""
Created on Mon Jan 24 11:50:20 2022

@author: Pappa
"""

class Transaction:

    trans_id = 0
    user_id = 0
    trans_date = ""
    acc_num = 0    
    trans_amount = 0


    def __init__(self, user_id, acc_num, trans_amount, trans_date):
        self.user_id = user_id
        self.acc_num = acc_num
        self.trans_amount = trans_amount
        self.trans_date = trans_date
        
    # represents the class objects as a string
    def __str__(self):
        if self.trans_amount < 0:
            return "\nDate: {}\nAccount Number: {}\nWithdrawn Amount: {}".format( self.trans_date, self.acc_num, self.trans_amount * 1)
        else:
            return "\nDate: {}\nAccount number: {}\nDeposited amount: {}".format( self.trans_date, self.acc_num, self.trans_amount)