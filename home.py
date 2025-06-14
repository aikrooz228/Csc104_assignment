import streamlit as st

st.set_page_config(page_title="Bank App Home", layout="centered")

st.title("🏦 Welcome to the Bank App")

st.subheader("Choose your account type:")

option = st.selectbox("Go to page:", ["-- Select --", "💰 Savings Account", "💼 Current Account"])

if option == "💰 Savings Account":
    st.switch_page("pages/saving.py")

elif option == "💼 Current Account":
    st.switch_page("pages/current.py")
else:
    st.write("Please select an account type to proceed.")