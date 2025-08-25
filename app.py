import streamlit as st
import pandas as pd

if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_parquet('Indian_Kids_Screen_Time.parquet')

pg = st.navigation([
    st.Page("pages/pag1.py", title= "Dashboard", icon="😂"),
    st.Page("pages/pag2.py", title= "Forms", icon="❤️"),
    st.Page("pages/page3.py", title= "Filtro", icon="😁")
])

pg.run()