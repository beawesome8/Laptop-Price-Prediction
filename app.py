import streamlit as st
import pickle
import numpy as np

#import the model
pipe = pickle.load(open('pipe_RF.pkl','rb'))
laptops_df = pickle.load(open('laptops_df.pkl','rb'))

st.title("laptop Price Predctor")

#Creating List for user to input from

#Model
Model = st.selectbox('Model', laptops_df['Model'].unique())

# type of laptop
Series = st.selectbox('Series', laptops_df['Series'].unique())

# RAM
Ram = st.selectbox('Ram (GB)', [2,4,6,8,12,16,24,32,64])

# Weight
Weight = st.number_input('Laptop Weight (kg)')

# Touchscreen
Touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
IPS = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
Screen_Size = st.number_input('Screen Size', min_value=1.0, value=15.6)

# Resolution
Resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800',
                                        '2560x1600','2560x1440','2304x1440'])
#CPU
Cpu = st.selectbox('CPU',laptops_df['Cpu brand'].unique())

# HDD
HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# SSD
SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

# GPU 
GPU = st.selectbox('GPU',laptops_df['Gpu Brand'].unique())

# OS 
OS = st.selectbox('OS',laptops_df['OS'].unique())

if st.button('Predict Price'):
    # query
    PPI = None
    if Touchscreen == 'Yes':
        Touchscreen = 1 
    else:
        Touchscreen = 0
        
    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0
        
    X_res = int(Resolution.split('x')[0])
    y_res = int(Resolution.split('x')[1])
    PPI = ((X_res**2) + (y_res**2))**0.5/Screen_Size
    query = np.array([Model, Series, Ram, Weight, Touchscreen, IPS, PPI, Cpu, HDD, SSD, GPU, OS])
    
    query = query.reshape(1,12)
    st.title(f'Predicted Price: {int(np.exp(pipe.predict(query)[0]))} Euros')
