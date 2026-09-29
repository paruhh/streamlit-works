import streamlit as st
st.title("DIVISION")

num1 = st.number_input("Enter number 1", min_value=0)
num2 = st.number_input("Enter number 2", min_value=0)
st.write(num1)
st.write(num2)

btn = st.button("DIVIDE")
if btn:
    s = num1 / num2
    st.write("quotient is", s)
