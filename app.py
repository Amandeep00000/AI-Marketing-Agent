import streamlit as st
from agent import run_agent
from automation import save_output

st.title(" AI Marketing Agent")

user_input = st.text_input("Enter your business idea")

if st.button("Generate"):
    result = run_agent(user_input)
    
    st.write("### Output:")
    st.write(result)
    
    save_output(result)