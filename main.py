"""
Created on Tue Jan 27 11:21:09 2022

@author: Pappa
"""

from bank import Bank
bank = Bank()
bank._load()



def main():
    execute = True
    while(execute):
        # Keeping The Menu Alive
        print("\n1. List All Existing Customers\n2. Search For A Customer\n3. Add New Customer")
        print("4. Update Customer Information\n5. Remove Customer\n6. Create Account")
        print("7. Transaction\n8. Terminate Account\n9. Exit")

        try:
            choice = int(input("Choose One Of The Alternatives: "))
            if len(str(choice)) != 1:
                print("Please Choose Aleternatives 1-9")
        except ValueError:
            print("Invalid Entry")
            
            

        # Show Bank's All Customers
        if choice == 1:
            print("\nNames And Social Security Number For All Customers")
            for x in bank.customers:
                print(x)



        # Print Customer's Details
        elif choice == 2:
            pnr = pnr_input()
            if pnr != 0:
                print(bank.get_customer(pnr))



        # Add New Customer
        elif choice == 3:
            pnr = pnr_input()
            if pnr != 0:
                first_name = str(input("\nEnter First Name: "))
                last_name = str(input("\nEnter Last Name: "))
                if bank.add_customer(first_name, last_name, pnr):
                    print("\nCustomer With Social Security Number {} Added.".format(pnr))
                else:
                    print("\nThis Social Security Number Already Exists.")                    
                    
                

        # Update Customer's Name
        elif choice == 4:
            pnr = pnr_input()
            if pnr != 0:
                first_name = str(input("\nEnter First Name: "))
                last_name = str(input("\nEnter Last Name: "))
                if bank.change_customer_name(first_name + " " + last_name, pnr):
                    print("\nCustomer Name Is Updated.")
                else:
                    print("\nCustomer Does Not Exist.")
                    
                    

        # Remove Customer
        elif choice == 5:
            pnr = pnr_input()
            if pnr != 0:
                found_cust_rem = bank.remove_customer(pnr)
                if found_cust_rem:
                    print("\nCustomer With Social Security Number {} Is Removed.".format(pnr))
                    if len(found_cust_rem) == 3:
                        print("\nTerminated Accounts:")
                        print(found_cust_rem[0])
                        print(found_cust_rem[1])
                    elif len(found_cust_rem) == 2:
                        print("\nTerminated Accounts:")
                        print(found_cust_rem[0])
                    print("\n${} Is Refunded.".format(found_cust_rem[-1]))
                else:
                    print("Customer Does Not Exist.")
                    


        # Create Account For An Existing Customer
        elif choice == 6:
            pnr = pnr_input()
            if pnr != 0:
                acc_num = bank.add_account(pnr)
                if acc_num != -1:
                    print("Account With Account Number {} Is Created.".format(acc_num))
                else:
                    print("Customer Already Has 2 Accounts.\nPlease Contact The Bank.")
                    
                    

        # Transactions 
        elif choice == 7:
            print("\n1. Withdraw\n2. Deposit\n3. Return To Main Menu")

            try:
                trans_choice = int(input("Choose One Of The Options: "))
                if len(str(trans_choice)) != 1:
                    print("Please Choose Aleternatives 1, 2 Or 3")
            except ValueError:
                print("Invalid Entry")
        
            # (Withdraw Or Deposit)
            if trans_choice == 3:
                return main()
            elif trans_choice == 1 or 2:
                pnr = pnr_input()
                if pnr != 0:
                    if display_customer_accounts(pnr):
                        acc_num = acc_num_input()
                        if acc_num != 0:
                            try:
                                trans_amount = float(input("Enter Amount: "))
                                if trans_amount > 0:
                                    if trans_choice == 1:
                                        if bank.withdraw(pnr, acc_num, trans_amount):
                                            print("\n${} Withdrawn From The Account {}.".format(trans_amount, acc_num))
                                        else:
                                            # Error Message If The Withdraw Amount Requested Is more Than Current Balance
                                            print("\nWithdraw Failed. No Sufficient Found Available.\nPlease Contact The Bank.")
                                    else:
                                        if bank.deposit(pnr, acc_num, trans_amount):
                                            print("\n${} Deposited To The Account {}.".format(trans_amount, acc_num))
                                        else:
                                            print("\nDeposit Failed. Please Contact The Bank.")
                                else:
                                    print("Invalid Entry. Please Enter Positive Amount Only")

                            except ValueError:
                                print("Invalid Entry. Digits Only.")



        # Terminate Account
        elif choice == 8:
            pnr = pnr_input()
            if pnr != 0:
                if display_customer_accounts(pnr):
                    acc_num = acc_num_input()
                    if acc_num != 0:
                        print(bank.remove_account(pnr, acc_num))



        # Exit The Application
        elif choice == 9:
            print("\nPress 'Enter' To Exit ...")
            exit()


############################################



# Display All Accounts Specific To A Customer
def display_customer_accounts(pnr):
    found_accs = bank.get_cust_accs(pnr)
    if found_accs:
        print("\nCustomer's Account(s):")
        for x in found_accs:
            print(x)
    else:
        print("\nCustomer With Social Security Number {} Has No Account.".format(pnr))
        return False
    return True



# User Social Security Number Input
def pnr_input():
    try:
        pnr = int(input("\nEnter Customer Social Security Number (8 digits): "))
        if len(str(pnr)) != 8:
            print("\nYou Need To Enter Social Security Number With 8 Digits")
            return 0
        return pnr        
    except ValueError:
        print("\nSocial Security Number Contains Digits Only!")
    return 0



# User Accoiunt Number Input
def acc_num_input():
    try:
        acc_num = int(input("Enter Account Number (4 Digits): "))
        if len(str(acc_num)) != 4:
            print("You Need To Enter Account Number With 4 Digits")
            return 0
        return acc_num
    except ValueError:
        print("Account Number Contains Numbers Only!")
    return 0



"""
The
if __name__ == “main”:
is used to execute some code only if the file was run directly, and not imported
"""
if __name__ == "__main__":
    main()
