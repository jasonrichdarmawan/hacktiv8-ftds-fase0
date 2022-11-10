import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='FIFA 2022',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Fifa 2022 Player Rating Prediction')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisa Dataset FIFA 2022')

    # Membuat Deskripsi
    st.write('Page ini dibuat oleh *Jason Rich Darmawan Onggo Putra*')

    # Menambahkan Gambar
    image = Image.open('./images/istockphoto-1253858343-170667a.jpeg')
    st.image(image, caption='FIFA 2022')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Snytax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana.
    Dataset yang digunakan adalah dataset FIFA 2022.
    Dataset ini berasal dari web sofifa.com
    '''
    data = pd.read_csv('./data/P1W1D1PM - Machine Learning Problem Framing.csv')
    st.dataframe(data)

    # Membuat BarPlot
    st.write('#### Plot Attacking WorkRate')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(data=data, x='AttackingWorkRate')
    st.pyplot(fig)
    del fig

    # Membuat Histogram
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['Overall'], bins=30, kde=True)
    st.pyplot(fig)
    del fig

    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram berdasarkan Input User')
    # st.selectbox | st.radio
    pilihan = st.selectbox('Pilih Column:', ['Age', 'Weight', 'Height', 'ShootingTotal'])
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Plotly Plot - ValueEUR dengan Overall')
    fig = px.scatter(data, x='ValueEUR', y='Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)

# streamlit run eda.py
if __name__ == '__main__':
    run()