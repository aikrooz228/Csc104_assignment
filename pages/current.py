import sys
import os
import datetime
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from current_account import CurrentAccount

st.set_page_config(page_title="Current Account", layout="centered")
st.title("Current Account")


if "current" not in st.session_state:
    st.session_state.current = CurrentAccount(10000)



current=st.session_state.current


with st.form("Current Account"):
    amount = st.number_input("Enter Amount",min_value=0, step=100, format="%d", help="Enter a positive amount to deposit or withdraw.")
    operation=st.selectbox("Deposit or Withdraw",("Deposit","Withdraw"))
    submit=st.form_submit_button("Submit")
    if submit:
        if operation == "Withdraw":
            with st.spinner("Processing..."):
                if amount > current.balance:
                    st.error("Insufficient Funds")
                else:
                    current.withdraw(amount)
                    st.success(f'Transaction Successful! New balance is: {current.balance}')

        elif operation == "Deposit":
            with st.spinner("Processing..."):
                if amount <=0:
                    st.error("Deposit amount must be greater than zero.")
                else:
                    current.deposit(amount)
                    st.success(f'Transaction Successful! New balance is: {current.balance}')