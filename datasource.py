"""
Created on Thu Jan 27 01:23:27 2022

@author: Pappa
"""

class Datasource:
    
    customers_table = "custs_table.txt"

    def datasource_conn(self):
        try:
            f = open(self.customers_table)
            conn_state = (True, "Connection Successful", self.customers_table)
        except:
            conn_state = (False, "Connection Failed. Check If Datasource Exist", self.customers_table)
        finally:
            f.close(self.customers_table)        
        return conn_state
    
    
    
    # Read Rows Of Data From Data Source And Return Values As Lists
    def get_existing_customers(self):
        data = []

        try:
            f = open(self.customers_table, "r")
            for x in f:
                row = x.strip().split(":")
                data.append(row)
        finally:
            f.close()
        return data



    # Calculate Highest Customer ID Based On Number Of Rows In Data Source File 
    def get_last_id(self):
        id = []        

        try:
            f = open(self.customers_table, "r")
            for x in f:
                row = x.strip().split(":")
                id.append(row[0])
            n_last_id = id[-1]
            last_id =int(n_last_id)
        finally:
            f.close()
        
        return last_id
    
    
    
    # Add New Row (ie. Customer) To cust_table File
    def add_row_customers(self, id, name, cust_pnr):
        new_row = str(id) + ":" + name + ":" + str(cust_pnr)

        try:
            f = open(self.customers_table, "a")
            f.write("\n" + new_row)
        finally:
            f.close()
            
            

    # Update Customer's First and Last Name
    def update_row_name(self, name, cust_pnr):
        f = open(self.customers_table, "r")
        rows = f.readlines()
        f.close()

        for row in rows:
            if str(cust_pnr) in row:
                index = rows.index(row)
                full_name = row.split(":")[1]
                new_row = row.replace(full_name, name)
                rows[index] = new_row

        f = open(self.customers_table, "w")
        f.writelines(rows)
        f.close()
        
        

    #Add Account To Row (ie. Customers) In cust_table File
    def update_row_acc(self, account, cust_pnr):
        f = open(self.customers_table, "r")
        rows = f.readlines()
        f.close() 

        for row in rows:
            if str(cust_pnr) in row:
                index = rows.index(row)
                rows[index] = row.rstrip("\n")
                rows[index] = rows[index] + account

        f = open(self.customers_table, "w")
        f.writelines(rows)
        f.close()



    # Delete Row (ie. Customer) In cust_table.txt
    def remove_row(self, cust_pnr):
        f = open(self.customers_table, "r")
        rows = f.readlines()
        f.close()

        for row in rows:
            if str(cust_pnr) in row:
                index = rows.index(row)
                del rows[index]
  
        rows[len(rows)-1] = rows[len(rows)-1].rstrip("\n")

        f = open(self.customers_table, "w")
        f.writelines(rows)
        f.close()
        
        

    # Delete An Account From A Row (ie. Customer) In cust_table.txt
    def remove_row_acc(self, acc_num):
        f = open(self.customers_table, "r")
        rows = f.readlines()
        f.close()

        for row in rows:
            if str(acc_num) in row:
                index = rows.index(row)
                if "#" in row:
                    customer_info = row.strip().split("#")[0].split(":")[:3]
                    first_acc = row.strip().split("#")[0].split(":")[3:]
                    second_acc = row.strip().split("#")[1].split(":")

                    new_row_customer = customer_info[0] + ":" + customer_info[1] + ":" + customer_info[2]
                    
                    if str(acc_num) not in first_acc:
                        new_row_acc = ":" + first_acc[0] + ":" + first_acc[1] + ":" + first_acc[2]
                    else:
                        new_row_acc = ":" + second_acc[0] + ":" + second_acc[1] + ":" + second_acc[2]
                    new_row = new_row_customer + new_row_acc

                else:
                    customer_info = row.strip().split(":")[:3]
                    new_row = customer_info[0] + ":" + customer_info[1] + ":" + customer_info[2]
                
                if row != rows[-1]:
                    new_row += "\n"
                    
                rows[index] = new_row
                f = open(self.customers_table, "w")
                f.writelines(rows)
                f.close()
                return True
        return False
                
