"""
Created on Mon Jan 24 14:17:27 2022

@author: Pappa
"""


#import datetime
from customer import Customer
from account import Account
from datasource import Datasource



class Bank:

    conn_state = Datasource()
    customer_details = []
    customers = []
    accounts = []

   

    def _load(self):
        '''
        This Protected Function Gets The Customers' ToTal Information
        From A Function In Datasource And Then Loads This Info Into
        "customer_details" Array List
        '''
        self.customer_details = self.conn_state.get_existing_customers()
        self._load_customers()
        self._load_accounts()



    
    def _load_customers(self):
        '''
        This Protected Function Retrives Only A Selected Part Of The Information For Each Customer
        From The "customer_details" Array List.
        Extracted Info: Customer's ID, Name, And Social Security Number.
        Note That The Index Positions Denoted In Account() Is Based On The Arrangement Of Items
        In Each Reacord (ie. Row) In The Data Source.
        '''
        for x in self.customer_details:
            try:
                # Wrong Order Of Items, Giving Error                
                customer = Customer(int(x[0]), x[1].split()[0], x[1].split()[1], int(x[2]))
                #customer = Customer((x[0]), int(x[2]), x[1].split()[0], x[1].split()[1])
                self.customers.append(customer)
            except:
                print("Error Loading {}.".format(x))
                
                


    def _load_accounts(self):
        '''
        This Protected Function Retrives Only A Selected Part Of The Information For Each Customer
        From The "customer_details" Array List.
        Extracted Info: Account Numbers, Type Of Accounts, And Account Balance For Each Customer.
        Note That The Index Positions Denoted In Account() Is Based On The Arrangement Of Items
        In Each Reacord (ie. Row) In The Data Source.
        '''
        account_details = {}

        for x in self.customer_details:
            account_details[x[0]] = x[3:]
            # Ommit The First Three Parts Of The Account Record

        for x, y in account_details.items():
            if len(y) > 3:
                # True Only When Account Details Are Entered
                account_one = Account(int(x), int(y[0]), y[1], float(y[2].split("#")[0]))
                self.accounts.append(account_one)                
                account_two = Account(int(x), int(y[2].split("#")[1]), y[3], float(y[4]))                
                self.accounts.append(account_two)
            elif len(y) == 3:
                account_one = Account(int(x), int(y[0]), y[1], float(y[2]))
                self.accounts.append(account_one)
            else:
                pass

                
            
    # Show Customer Details For Customer Selected By PNR
    def get_customer(self, pnr):
        found_cust = []
        # Loop In Loop For Finding Data Using Two Attributes
        for x in self.customers:            
            if pnr == x.cust_pnr:
                # Finding The Customer By Comparing The Given PNR To Customers' PNR In The Data Source
                found_cust.append(x.first_name + " " + x.last_name)                
                found_cust.append(x.cust_pnr)

                for y in self.accounts: # Finding Customer's Accounts By Comparing Customer ID With The Account's User ID
                    if x.cust_id == y.user_id:
                        # The Arrangement Of Items Below Is Based On Specifications Given By User Story
                        account = "Account Number: " + str(y.acc_num) + ", Account Balance: " + str(y.acc_balance)
                        found_cust.append(account)

                return found_cust
            
        return "\nCustomer With Social Security Number {} Does Not Exist".format(pnr)
    
    

    # Add A New Customer
    def add_customer(self, first_name, last_name, pnr):

        for customer in self.customer_details:
            if str(pnr) in customer:
                return False           
        
        # Calculating The Next Customer ID    
        customer_id = int(self.conn_state.get_last_id()) + 1
        name = first_name + " " + last_name

        self.customer_details.append([customer_id, name, pnr])
        self.customers.append(Customer(customer_id, first_name, last_name, pnr))
        self.conn_state.add_row_customers(customer_id, name, pnr)
        return True

    

    # Update Existing Customer
    def change_customer_name(self, name, pnr):
        for x in self.customers:
            if pnr == x.cust_pnr:
                x.first_name = name.split()[0]
                x.last_name = name.split()[1]
                self.conn_state.update_row_name(name, pnr)
                self.customer_details = self.conn_state.get_existing_customers()
                return True
        return False
    
    

    # Remove Existing Customer   
    def remove_customer(self, pnr):
        refunded_balance = 0.0
        rem_cust = []
        refund = []

        for x in self.customers:
            if pnr == x.cust_pnr:
                index = self.customers.index(x)
                self.customers.pop(index)

                for y in self.accounts:
                    if x.cust_id == y.user_id:
                        refund.append(y)
                        rem_cust.append(self.accounts.index(y))
                        refunded_balance += y.acc_balance
                
                for z in reversed(rem_cust):
                    self.accounts.pop(z)

                self.conn_state.remove_row(pnr)
                self.customer_details = self.conn_state.get_existing_customers()
        
                refund.append(refunded_balance)
        return refund
    
    
    
    # Calculate New Account Number
    def get_new_acc_num(self):
        acc_numbers = []
        new_acc_num = 0

        for x in self.accounts:
            acc_numbers.append(x.acc_num)

        for n in acc_numbers:
            if int(n) > new_acc_num:
                new_acc_num = int(n)

        return new_acc_num + 1    
    
    
    
    # Add A New Account For An Existing Customer
    def add_account(self, pnr):
        temp_acc = []
        acc_num = self.get_new_acc_num()
        acc_type = "debit account"
        acc_balance = 0.0

        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if x.cust_id == y.user_id:
                        temp_acc.append(y)
                    
                if len(temp_acc) == 2:
                    return -1
                elif len(temp_acc) == 1:
                    # The Arrangement Of Items Below Is Based On Specifications Given By User Story
                    acc_row = "#" + str(acc_num) + ":" + acc_type + ":" + str(acc_balance) + "\n"
                    new_acc = Account(x.cust_id, acc_num, acc_type, acc_balance)
                    self.accounts.append(new_acc)
                    self.conn_state.update_row_acc(acc_row, pnr)
                    return acc_num
                else:
                    acc_row = ":" + str(acc_num) + ":" + acc_type + ":" + str(acc_balance) + "\n"
                    new_acc = Account(x.cust_id, acc_num, acc_type, acc_balance)
                    self.accounts.append(new_acc)
                    self.conn_state.update_row_acc(acc_row, pnr)
                    return acc_num
        return -1



    # List All Accounts Belonging To A Customer
    def get_cust_accs(self, pnr):
        found_accs = []

        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if x.cust_id == y.user_id:
                        # The Arrangement Of Items Below Is Based On Specifications Given By User Story
                        acc_info = "Account Number: " + str(y.acc_num) + ", Account Balance: " + str(y.acc_balance)
                        found_accs.append(acc_info)
        return found_accs
    
    

    # Find Account Using PNR Or Account Number
    def get_account(self, pnr, acc_num):
        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if acc_num == y.acc_num and x.cust_id == y.user_id:
                        return "\nAccount Number: {}\nAccount type: {}\nAccount Balance: {}".format(acc_num, y.acc_type, y.acc_balance)
                return "\nAccount Number {} Was Not Found.".format(acc_num)
        return "\nCustomer With Social Security Number {} Does Not Exist.".format(pnr)
    


    # Remove Existing Account
    def remove_account(self, pnr, acc_num):
        rem_account = []
        refunded_amount = 0.0

        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if acc_num == y.acc_num and x.cust_id == y.user_id:
                        refunded_amount = y.acc_balance
                        rem_account.append(self.accounts.index(y))
                if not rem_account:
                    return "\nAccount With Account Number {} Was Not Found.".format(acc_num)
                else:
                    for z in rem_account:
                        if self.conn_state.remove_row_acc(acc_num):
                            self.accounts.pop(z)
                            return "\nAccount Closed. ${} Was Refunded.".format(refunded_amount)
                        else:
                            return "\nCould Not Remove Account. Please Contact The Bank."
        return "\nNo Customer With Social Security Number {} Was Found.".format(pnr)

    

    # Deposit Into An Account  
    def deposit(self, pnr, acc_num, amount):
        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if acc_num == y.acc_num and x.cust_id == y.user_id:                        
                        y.acc_balance += amount
                        return True
        return False
    
    

    # Withdraw From An Account
    def withdraw(self, pnr, acc_num, amount):
        for x in self.customers:
            if pnr == x.cust_pnr:
                for y in self.accounts:
                    if acc_num == y.acc_num and x.cust_id == y.user_id:
                        if y.acc_balance >= amount:
                            y.acc_balance -= amount
                            return True
        return False
