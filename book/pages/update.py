import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("UPDATE RECORD")

i=st.number_input("Enter book id",min_value=0)

a=st.text_input("Title")

f=st.text_input("Author")

c=st.number_input("Price",min_value=0)

d=st.text_input("Language")

e=st.number_input("Pages",min_value=0)

# button()
btn=st.button("UPDATE")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.update(a,f,c,d,e,i)
    print(record)
    if record:
        st.success("Updated Record Successfully")
    else:
        st.error("No Records Found")
