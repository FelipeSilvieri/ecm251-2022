## Nome: Felipe Matos Silvieri
## RA: 20.00314-5
import streamlit as st


st.markdown("<h1 style='text-align: center; color: grey;'>ÁREA DE LOGIN</h1>", unsafe_allow_html=True)

st.text_input("Usuario")
st.text_input("Senha")
st.button("login")