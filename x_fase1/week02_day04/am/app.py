import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox(label='Pilih Halaman', options=('EDA', 'Predict A Player'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()