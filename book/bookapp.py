import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete
st.title("WELCOME TO LIBRARY APP")

b=BookListCreateRetrieveUpdateDelete()
tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.write('ADD')

with tab2:
    st.write('READ')

with tab3:
    st.write('RETRIEVE')

with tab4:
    st.write('UPDATE')

with tab5:
    st.write('DELETE')
