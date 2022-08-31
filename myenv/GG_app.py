import streamlit as st
st.set_page_config(layout="wide") # Increase page width for app
import pandas as pd
import sys
import os
import xlrd
import openpyxl
import requests
import numpy
import datetime

@st.cache(show_spinner=False)
def episode_list():
    url = 'https://github.com/abdelkaderalia/GG_app/blob/main/myenv/GG_episodes.xlsx?raw=true'
    r = requests.get(url)
    data = r.content
    df = pd.read_excel(data)
    return df

def return_episode(vibe_name,time_name):
    row = df.query('vibe == @vibe_name & time_year == @time_name').sample(n=1)
    selector = (row.iloc[0]['season'],row.iloc[0]['num_inseason'])
    num = row.iloc[0]['num_overall']
    title = row.iloc[0]['title']
    air_date = row.iloc[0]['air_date'].strftime("%B %e, %Y")
    viewers = row.iloc[0]['US_viewers_M']
    output = [selector,num,title,air_date,viewers]
    return output

#### App starts here
if __name__ == "__main__":
    #st.markdown('<h2 align="center">Gilmore Girls Episode Selector</h2>', unsafe_allow_html=True) # Add app title
    st.title('Gilmore Girls Episode Selector')
    df = episode_list()
    vibes = df['vibe'].unique().tolist()
    times = df['time_year'].unique().tolist()
    vibes.insert(0,'')
    times.insert(0,'')
    vibe_name = st.sidebar.selectbox("What's the vibe?", vibes)
    time_name = st.sidebar.selectbox("What time of year?", times)

    if vibe_name!='' and time_name!='':
        output = return_episode(vibe_name,time_name)
        selector = output[0]
        num = output[1]
        title = output[2]
        air_date = output[3]
        viewers = output[4]

        col1,col2 = st.columns(2)
        col1.success(f'Check out Season {selector[0]}, Episode {selector[1]}!')

        st.write(f'Episode Title: {title}')
        st.write(f'Episode Number Overall: {num} out of 153')
        st.write(f'Original Air Date: {air_date}')
        st.write(f'Number US Viewers: {viewers} million')
