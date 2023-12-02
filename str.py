import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("mn.csv")
col_names = df.columns
col_names = list(col_names)
print(col_names)
