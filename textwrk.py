import streamlit as st

#number_input()
#text_input()

num1=st.number_input("Enter number 1",min_value=0)
num2=st.number_input("Enter number 2",min_value=0)
#st.write(num1)
#st.write(num2)

t=st.text_input("Enter name")
#st.write(t)


#date_input
date=st.date_input("Enter date")
# st.write(date)


# button()
btn=st.button("click")
if btn:
    st.write(num1)
    st.write(num2)
    st.write(t)
    st.write(date)