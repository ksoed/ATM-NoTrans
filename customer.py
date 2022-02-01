"""
Created on Mon Jan 24 11:18:38 2022

@author: Pappa
"""

class Customer:

    cust_id = 0
    cust_pnr = 0
    first_name = ""
    last_name = ""

    def __init__(self, cust_id, cust_pnr, first_name, last_name):
        self.cust_id = cust_id
        self.cust_pnr = cust_pnr
        self.first_name = first_name
        self.last_name = last_name
        
    # represents the class objects as a string
    def __str__(self):        
        #return self.cust_id + self.first_name + " " + self.last_name + " - " + str(self.cust_pnr)
        return self.first_name + " " + self.last_name + " " + str(self.cust_pnr)