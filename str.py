import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("mn.csv")
col_names = df.columns
df['lat'] = df.start_lat
df['lon'] = df.start_lng


st.title("HSE Project")
st.write("Dashboard for project")
st.map(df)
hd = df[:20].values.tolist()
hd


