import streamlit as st
from util import encode,predict

st.set_page_config(page_title="Default Risk Prediction",
                   page_icon=":moneybag:", layout="wide")
st.title("Default Risk Prediction")

person_info, credit_hist = st.columns(spec=2)

with person_info:
    st.header("Personal Information")
    name = st.text_input("Name", placeholder="Enter Your Name", label_visibility="hidden")
    age = st.number_input("Age", min_value=18, max_value=100, value=25, step=1, placeholder="Enter Your Age", label_visibility="hidden")
    gender = st.selectbox("Gender", options=("Male", "Female"), index=None, placeholder="Gender", label_visibility="hidden")
    mstat = st.selectbox("Marital Status", options=("Married", "Single", "Others"), index=None, placeholder="Marital Status", label_visibility="hidden")
    edu = st.selectbox("Education", options=("Graduate School", "University", "High School", "Others"), index=None, placeholder="Education", label_visibility="hidden")
    limit_bal = st.number_input("Credit Limit", min_value=0, max_value=100000000000, value=None, step=100, placeholder="Limit Balance", label_visibility= "hidden")

with credit_hist:
    st.header("Credit History")
    stat, bill, pay = st.columns(3)
    # Payment Status
    PAY_1 = stat.number_input("Repayment Status (Current Month)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")
    PAY_2 = stat.number_input("Repayment Status (1 Month Ago)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")
    PAY_3 = stat.number_input("Repayment Status (2 Month Ago)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")
    PAY_4 = stat.number_input("Repayment Status (3 Month Ago)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")
    PAY_5 = stat.number_input("Repayment Status (4 Month Ago)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")
    PAY_6 = stat.number_input("Repayment Status (5 Month Ago)", min_value=-2, max_value=800000, value=None, placeholder="Repayment delay")

    #Bill Amount
    BILL_AMT1 = bill.number_input("Bill Amount (Current Month)", min_value=-2, max_value=800000, value=None, step=100, placeholder="Bill Amount")
    BILL_AMT2 = bill.number_input("Bill Amount (1 Month Ago)", min_value=-2, max_value=800000, value=None, step=100, placeholder="Bill Amount")
    BILL_AMT3 = bill.number_input("Bill Amount (2 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Bill Amount")
    BILL_AMT4 = bill.number_input("Bill Amount (3 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Bill Amount")
    BILL_AMT5 = bill.number_input("Bill Amount (4 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Bill Amount")
    BILL_AMT6 = bill.number_input("Bill Amount (5 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Bill Amount")

    #Payment Amount
    PAY_AMT1 = pay.number_input("Payment Amount (Current Month)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")
    PAY_AMT2 = pay.number_input("Payment Amount (1 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")
    PAY_AMT3 = pay.number_input("Payment Amount (2 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")
    PAY_AMT4 = pay.number_input("Payment Amount (3 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")
    PAY_AMT5 = pay.number_input("Payment Amount (4 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")
    PAY_AMT6 = pay.number_input("Payment Amount (5 Month Ago)", min_value=-2, max_value=800000, value=None,step=100, placeholder="Payment Amount")

btn_pred = st.button("Predict Default Risk !", use_container_width=True)

features = [limit_bal,
            encode("GENDER", gender),
            encode("EDUCATION", edu),
            encode("MARRIAGE", mstat),age,
            PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
            BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
            PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]

if btn_pred:
    st.write("Prediction Success !")
    st.write(name)
    st.write(features)

    result = predict(features)
    st.write(result)

