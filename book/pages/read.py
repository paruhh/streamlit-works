import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("BOOK LIST")


b=BookListCreateRetrieveUpdateDelete()
records=b.list()

st.write("")
if records:
    st.table(records)  # print records as table format
else:
    st.info("No Records Found")