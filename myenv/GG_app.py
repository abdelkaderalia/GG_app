import streamlit as st
st.set_page_config(layout="wide") # Increase page width for app
import pandas as pd
import sys
import os
import xlrd
import openpyxl
import requests
import numpy

@st.cache(show_spinner=False)
def episode_list():
    url = 'https://github.com/abdelkaderalia/GG_app/blob/main/myenv/GG_episodes.xlsx?raw=true'
    r = requests.get(url)
    data = r.content
    df = pd.read_excel(data)
    return df

def return_episode(df,mood_name):
    row = df.query('Category == @mood_name').sample(n=1)
    episode = (row.iloc[0]['Season'],row.iloc[0]['Episode'])
    statement = f'Check out Season {episode[0]}, Episode {episode[1]}!'
    return statement

#### App starts here
if __name__ == "__main__":
    #st.markdown('<h2 align="center">Gilmore Girls Episode Selector</h2>', unsafe_allow_html=True) # Add app title
    st.title('Gilmore Girls Episode Selector')
    df = episode_list()
    moods = df['Category'].unique().tolist()
    moods.insert(0,'')
    mood_name = st.sidebar.selectbox("Choose your mood:", moods) # Store user selection for agency name

    if mood_name!='':
        selector = return_episode(df,mood_name)
        st.success(selector)
