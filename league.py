# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:10:43 2021

@author: leode
"""

import requests
import json
import streamlit as st
import pandas as pd

# App title
st.markdown('''
# League of Legends Champion Bios!

**Credits**
- App built by Leo Delima
- Built in `Python` using `streamlit`,`pandas`, and Riot's DDragon API
''')

# Sidebar
st.sidebar.subheader('Query parameters')
champlist = pd.read_csv('https://raw.githubusercontent.com/ninefourlion/league/main/LoL-Champions.csv')
champselect = st.sidebar.selectbox('Select a Champion you are interested in', champlist)

url = "http://ddragon.leagueoflegends.com/cdn/11.6.1/data/en_US/champion/"+champselect+".json"

response = requests.get(url)

response.json()

champRawData = json.loads(response.text)
crd = champRawData['data']



name = crd[champselect]['id']
lore = crd[champselect]['lore']
title = crd[champselect]['title']
imgurl = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"+champselect+"_0.jpg"

st.image(imgurl)

st.write(name, title)
st.write(lore)

