# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:05:00 2024

@author: Swazi.Modibe
"""

import sqlite3
import pandas as pd


df = pd.read_csv('C:\\Users\Swazi.Modibe\Desktop\ITDAA4 Project/heart.csv')
#df.columns=df.columns.str.strip()
connection=sqlite3.connect('Heart.db')
df.to_sql('heart.csv',connection,if_exists='replace')
connection.close

print(df)