import streamlit as st
import pandas as pd
from datetime import datetime
from claim_automation import submit_claim_form


st.title('Insurance Claims Filing App')

tab1, tab2 = st.tabs(["Fetch Claims", "Submit Claim"])

with tab1:
    st.write('All filed claims')
    df = pd.read_csv('../fastapi_app/data/claims_data.csv')
    st.table(df)
with tab2:
    st.write('Submit claims')
    claim_id = st.text_input(label='Claim ID')
    provider_name = st.text_input(label='Provider Name')
    patient_name = st.text_input(label='Patient Name')
    amount = st.text_input(label='Amount')
    filing_day = datetime.now()
    # st.text_input(label='Filing_day')
    address = st.text_input(label='Address')
    b = st.button('Submit')
    if b:
        print(claim_id)
        
        print('Submitting Claim request')
        submit_claim_form(claim_id, provider_name, patient_name,
                        amount, filing_day.strftime("%Y-%m-%d %H:%M:%S"), address)
        st.write('Claim submitted')
