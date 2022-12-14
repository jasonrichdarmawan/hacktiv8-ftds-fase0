import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import joblib
import json

# Load All Files
with open('./model/model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = joblib.load(file_1)

with open('./model/model_scaler.pkl', 'rb') as file_2:
  model_scaler = joblib.load(file_2)

with open('./model/model_encoder.pkl', 'rb') as file_3:
  model_encoder = joblib.load(file_3)

with open('./model/list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('./model/list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)

def run():
    # Membuat Form
    with st.form(key='form_parameters'):
        name = st.text_input(label='Name', value='')
        age = st.number_input(label='Age', 
                            min_value=16, 
                            max_value=60, 
                            value=25, 
                            step=1, 
                            help='Usia PPemain')
        height = st.number_input(label='Height', 
                                min_value=50, 
                                max_value=250, 
                                value=170)
        weight = st.number_input(label='Weight', 
                                min_value=50, 
                                max_value=150, 
                                value=70)
        price = st.slider(label='Price', 
                        min_value=0, 
                        max_value=10000000000,
                        step=1000000,
                        format="Rp%d",
                        value=0)
        st.markdown('---')

        attacking_work_rate = st.selectbox(label='AttackingWorkrate', 
                                        options={'Low', 'Medium', 'High'},
                                        index=1)
        defensive_work_rate = st.selectbox(label='DefensiveWorkRate',
                                        options={'Low', 'Medium', 'High'},
                                        index=1)
        st.markdown("---")

        pace = st.number_input(label='Pace', 
                            min_value=0, 
                            max_value=100, 
                            value=50)
        shooting = st.number_input(label='Shooting', 
                                min_value=0, 
                                max_value=100, 
                                value=50)
        passing = st.number_input(label='Passing', 
                                min_value=0, 
                                max_value=100, 
                                value=50)
        dribbling = st.number_input(label='Dribbling', 
                                    min_value=0, 
                                    max_value=100, 
                                    value=50)
        defending = st.number_input(label='Defending', 
                                    min_value=0, 
                                    max_value=100, 
                                    value=50)
        physicality = st.number_input(label='Physicality', 
                                    min_value=0, 
                                    max_value=100, 
                                    value=50)
        st.markdown('---')
        
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'Name': name,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Price': price,
        'AttackingWorkRate': attacking_work_rate,
        'DefensiveWorkRate': defensive_work_rate,
        'PaceTotal': pace,
        'ShootingTotal': shooting,
        'PassingTotal': passing,
        'DribblingTotal': dribbling,
        'DefendingTotal': defending,
        'PhysicalityTotal': physicality
    }

    if submitted:
        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)
        # Split between Numerical Columns and Categorical Columns

        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Feature Scaling and Feature Encoding

        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

        # Concate Numerical Columns and Categorical Columns

        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

        # Predict using Linear regression

        y_pred_inf = model_lin_reg.predict(data_inf_final)

        st.write('# Rating : ', str(int(y_pred_inf)))