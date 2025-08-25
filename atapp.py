import streamlit as st
import pandas as pd
import plotly.express as px

if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_parquet('Health_Risk_Dataset_Otimizado.parquet')

pg = st.navigation([
    st.Page("pages_ativ/pag1.py", title= "Dados", icon="📈"),
    st.Page("pages_ativ/pag2.py", title= "Forms", icon="➕"),
])

pg.run()