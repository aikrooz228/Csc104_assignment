import sys 
import os
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from saving_account import SavingAccount

import streamlit as st

st.set_page_config(page_title="BANK APP", layout="centered")
st.title("Saving Account")


if 'savings' not in st.session_state:
    st.session_state.savings = SavingAccount(1000)
if 'transaction_date' not in st.session_state or st.session_state.transaction_date != datetime.date.today():
    st.session_state.transaction_date = datetime.date.today()
    st.session_state.transaction_count = 0

savings = st.session_state.savings
MAX_AMOUNT = 500_000
MAX_DAILY_TRANSACTIONS = 3

with st.form("Saving Account"):
    amount = st.number_input("Enter Amount", min_value=0, step=100, format="%d")
    operation = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        
        if st.session_state.transaction_count >= MAX_DAILY_TRANSACTIONS:
            st.error("Daily transaction limit reached. Try again tomorrow.")
    
        elif amount > MAX_AMOUNT:
            st.error(f"Maximum allowed per transaction is ₦{MAX_AMOUNT:,}.")
        elif operation == "Withdraw":
            with st.spinner("Processing..."):
                if amount > savings.balance:
                    st.error("Insufficient Funds")
                elif amount <= 0:
                    st.error("Withdrawal amount must be greater than zero.")
                else:
                    savings.withdraw(amount, 10)
                    st.session_state.transaction_count += 1
                    st.success(f"Transaction Successful! New balance is: {savings.balance}")
        elif operation == "Deposit":
            with st.spinner("Processing..."):
                if amount <= 0:
                    st.error("Deposit amount must be greater than zero.")
                else:
                    savings.deposit(amount)
                    st.session_state.transaction_count += 1
                    st.success(f"Transaction Successful! New balance is: {savings.balance}")

st.info(f"Today's transactions: {st.session_state.transaction_count}/{MAX_DAILY_TRANSACTIONS}")