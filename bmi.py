# # body mass index calculator using messages info,success,warning,error
import streamlit as st


w=st.number_input("Weight in kg",min_value=0)
h=st.number_input("Height in cm",min_value=0)



btn=st.button("Calculate BMI")
if btn:   ## s=num1+num2
    bmi=w/((h/100)**2)
    st.write("BMI",bmi)
    if bmi<=18.4:
        st.info("Underweight")

    elif bmi>=18.5 and bmi<=24.9:
        st.success("Normal")

    elif bmi>=25.0 and bmi<=39.9:
        st.warning("Overweight")

    else:
        st.error("Obesity")






