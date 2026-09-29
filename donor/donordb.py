# Blood Donor Management System using Python, MySQL and Streamlit
# Create a MySQL database named blooddb and create a table named donor to store blood donor details.
# The donor table should contain the following fields:


# id – Integer, Primary Key, Auto Increment
# name – Donor name
# bloodgroup – Blood group
# phone – Phone number, should be unique
# city – City
# last_donation – Date of last donation


# Create a Python class to perform database operations on the donor table.
# The class should contain methods to:
# Add a new donor
# Retrieve all donors
# Retrieve a donor using ID
# Update donor details
# Delete a donor using ID
# Create a Streamlit interface to perform these operations through a user-friendly interface.


import mysql.connector
class DonorAddReadRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="Arunima",host="localhost",database="donor_db")
        self.cursor=self.con.cursor()
        print("Successfully connected")

    def read(self):
        query = "select * from donor"
        self.cursor.execute (query)
        records = self.cursor.fetchall()
        if records:
            return records  ## return is used for returning the records to read.py file
            # for row in records:
            #     print(row)

        else:
            print("record not found")

    def create(self,name,bloodgroup,phone_number,city,last_donation):
        query="insert into donor(name,bloodgroup,phone_number,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,bloodgroup,phone_number,city,last_donation)
        self.cursor.execute(query,data)
        self.con.commit() # permenently save data into database
        print("Inserted data successfully")


    def retrieve(self,id):
        query="select * from donor where id=%s"
        data=(id,)  ## , is used in tuple to identify it is a sequence
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()  ## take one data or id- fetchone()
        if record:
            return(record)
        else:
            print("record not found")



    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)  ## , is used in tuple to identify it is a sequence
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
            print("data is deleted")
        else:
            return False
     #       print("no record found")


    def update(self,name,bloodgroup,phone_number,city,last_donation,id):
        query = "update donor set name=%s,bloodgroup=%s,phone_number=%s,city=%s,last_donation=%s where id=%s"
        data = (name,bloodgroup,phone_number,city,last_donation,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
            print("data is updated")
        else:
            return False
            print("no record found")


d=DonorAddReadRetrieveUpdateDelete()
# d.create('abhi','B+',8765434578,'plkd',"2024-08-6")
#d.read()
# d.retrieve(1)
#d.update("anju","A-",9876532789,'tvm','2025-04-9',3)
#d.delete(4)

