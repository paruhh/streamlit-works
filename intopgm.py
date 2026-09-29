import streamlit as st

# #title()
# st.title("Welcome To My App")
#
# #header()
# st.header("Main Heading")
#
# #subheader()
# st.subheader("Sub Heading")
#
# #write()
# st.write("My name is Arunima")

st.title("My Portfolio")

st.header("About Me")

st.write("My name is Arunima")
st.write("I am a python full stack developer")

st.header("My Skills")

st.subheader("Programming Languages")

st.write("     python,c,c++,java    ")

st.subheader("Frameworks")

st.write("Django")

st.subheader("Databases")

st.write("mysql,postgress")

# radio button
g=st.radio("Gender",['male','female'])
st.write(g)


c=st.checkbox("python")
st.write(c)

d=st.selectbox("places",['tvm','ekm'])
st.write(d)
