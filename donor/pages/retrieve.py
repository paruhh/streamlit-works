import streamlit as st
from donordb import DonorAddReadRetrieveUpdateDelete

st.title("RETRIEVE")

i=st.number_input("Enter donor id",min_value=0)

# button()
btn=st.button("RETRIEVE")
if btn:
    d = DonorAddReadRetrieveUpdateDelete()
    record=d.retrieve(i)
    print(record)
    if record:
        st.write("Name",record[1])
        st.write("Blood Group",record[2])
        st.write("Phone number",record[3])
        st.write("City",record[4])
        st.write("Last donation",record[5])
        st.success("Record Retrieved Successfully")

    else:
        st.error("No Records Found")

