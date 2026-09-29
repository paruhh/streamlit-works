import streamlit as st
from datetime import date
from donordb import DonorAddReadRetrieveUpdateDelete

st.title("READ")
d = DonorAddReadRetrieveUpdateDelete()
records=d.read()

st.write("")
if records:
    st.table(records)  # print records as table format
else:
    st.info("No Records Found")