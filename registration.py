import streamlit as st
from datetime import date

st.title("REGISTRAION FORM")

t=st.text_input("Name")

n=st.number_input("Age",min_value=0)

date=st.date_input("Date Of Birth",
                   min_value=date(1990,1,1),
                   max_value=date.today(),
                   value=date(2006,1,1))

email=st.text_input("Email")


g=st.radio("Gender",['Male','Female',])


d=st.selectbox("Courses",['Python','c++','c','java'])

# button()
btn=st.button("SUBMIT")
if btn:
    st.write("Name",t)
    st.write("Age",n)
    st.write("Date Of Birth",date)
    st.write("Email",email)
    st.write("Gender",g)
    st.write("Course",d)


