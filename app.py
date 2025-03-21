import streamlit as st
import pickle

#import the model
pipe = pickle.load(open('pipe.pkl','rb'))
laptops_df = pikcle.load(open('laptops_df.pkl','rb'))

st.title("laptop Price Predctor")

#Creating List for user to input from

#Model
Model = st.selectbox('Model', laptops_df['Model'].unique())

# type of laptop
Series = st.selectbox('Series', laptops_df['Series'].unique())

# RAM
Ram = st.selectbox('Ram (GB)', laptops_df['Ram'], [2,4,6,8,12,16,24,32,64])

# Weight
Weight = st.number_input()

# Touchscreen
Touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
IPS = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
Screen_Size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800',
                                        '2560x1600','2560x1440','2304x1440'])
#CPU
cpu = st.selectbox('CPU',laptops_df['Cpu brand'].unique())

# HDD
HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# SSD
SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

# GPU 
GPU = st.selectbox('GPU',laptops_df['Gpu Brand'].unique())

# OS 
OS = st.selectbox('OS',laptops_df['OS'].unique())

if st.button('Predict Price'):
    pass