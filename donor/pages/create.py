import streamlit as st
from datetime import date
from donordb import DonorAddReadRetrieveUpdateDelete

#name,bloodgroup,phone_number,city,last_donation
st.title("Add New Donor")


n=st.text_input("name")

b=st.text_input("bloodgroup")

p=st.number_input("Phone_number",min_value=0)

c=st.text_input("City")

l=st.date_input("Date",
                min_value=date(2000, 1, 1),
                max_value=date.today(),
                value=date.today())

# button()
btn=st.button("ADD DONOR")
if btn:
    d=DonorAddReadRetrieveUpdateDelete()
    d.create(n,b,p,c,l)
    st.success("Create Record Successfully")


