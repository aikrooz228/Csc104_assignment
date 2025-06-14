import sys 
import os
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from saving_account import SavingAccount

import streamlit as st

st.set_page_config(page_title="Savings Account", layout="centered")
st.title("Saving Account")
maximim_withdrawal = 500000

if 'savings' not in st.session_state:
    st.session_state.savings = SavingAccount(1000, maximim_withdrawal)


savings = st.session_state.savings


with st.form("Saving Account"):
    amount = st.number_input("Enter Amount",step=100, min_value=0, format="%d",)
    operation = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        if operation == "Withdraw":
            with st.spinner("Processing..."):
                if amount > savings.balance:
                    st.error("Insufficient Funds")
                elif amount > maximim_withdrawal:
                    st.error(f"Withdrawal limit exceeded. You can only withdraw up to {maximim_withdrawal}.")
                else:
                    savings.withdraw(amount)
                    st.success(f'Transaction Successful! New balance is: {savings.balance}')

        elif operation == "Deposit":
            with st.spinner("Processing..."):
                if amount <= 0:
                    st.error("Deposit amount must be greater than zero.")
                else:
                    savings.deposit(amount)
                    st.success(f'Transaction Successful! New balance is: {savings.balance}')