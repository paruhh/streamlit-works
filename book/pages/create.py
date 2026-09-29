import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete


st.title("Add New Record")


a=st.text_input("Title")

f=st.text_input("Author")

c=st.number_input("Price",min_value=0)

d=st.text_input("Language")

e=st.number_input("Pages",min_value=0)

# button()
btn=st.button("ADD")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(a,f,c,d,e)
    st.success("Create Record Successfully")





