import streamlit as st

from donordb import DonorAddReadRetrieveUpdateDelete
st.title("DELETE")

i=st.number_input("Enter donor id",min_value=0)

# button()
btn=st.button("DELETE")
if btn:
    d=DonorAddReadRetrieveUpdateDelete()
    record=d.delete(i)
    print(record)
    if record:
        st.success("Record Deleted Successfully")

    else:
        st.error("No Records Found")
