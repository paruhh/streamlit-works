import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("DELETE")

i=st.number_input("Enter book id",min_value=0)

# button()
btn=st.button("DELETE")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.delete(i)
    print(record)
    if record:
        st.success("Record Deleted Successfully")

    else:
        st.error("No Records Found")
