import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete
st.title("RETRIEVE RECORD")


i=st.number_input("Enter book id",min_value=0)

# button()
btn=st.button("RETRIEVE")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(i)
    print(record)
    if record:
        st.write("Title",record[1])
        st.write("Author",record[2])
        st.write("Price",record[3])
        st.write("Language",record[4])
        st.write("Page",record[5])
        st.success("Record Retrieved Successfully")

    else:
        st.error("No Records Found")
