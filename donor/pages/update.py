import streamlit as st
from datetime import date
from donordb import DonorAddReadRetrieveUpdateDelete

st.title("UPDATE")
i=st.number_input("Enter donor id",min_value=0)

n=st.text_input("Name")

b=st.text_input("Blood Group")

p=st.number_input("Phone Number",min_value=0)

c=st.text_input("City")

l=st.date_input("Last Donation",
                min_value=date(2000, 1, 1),
                max_value=date.today(),
                value=date.today())
# button()
btn=st.button("UPDATE")
if btn:
    d = DonorAddReadRetrieveUpdateDelete()
    record=d.update(n,b,p,c,l,i)
    print(record)
    if record:
        st.success("Updated Record Successfully")
    else:
        st.error("No Records Found")

