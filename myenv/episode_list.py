# Import packages and modules
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import os

import warnings
warnings.filterwarnings("ignore")

full = pd.DataFrame(columns=['Season','No.overall','No. inseason','Title','Directed by','Written by','Original air date','Prod.code','US viewers(millions)'])

for i in range(1,8):
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_Gilmore_Girls_episodes")[i]
    df.insert(0, 'Season', i)
    full = full.append(df)

full=full.drop(columns=['Prod.code'])
full['US viewers(millions)'] = full['US viewers(millions)'].str.replace(r"\[.*\]","")

os.chdir('/Users/alia/Documents/Github/GG_app/myenv')
full.to_csv('GG_episodes.csv',index=False)
