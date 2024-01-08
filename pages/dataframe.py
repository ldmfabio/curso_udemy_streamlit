import streamlit as st
from dataset import df

st.title('Dataset de Vendas')
st.dataframe(df)