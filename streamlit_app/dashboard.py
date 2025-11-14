import streamlit as st
import pandas as pd

st.title('Insurance Claims Filing App')
st.write('All filed claims')

df = pd.read_csv('../fastapi_app/data/claims_data.csv')

st.table(df)
