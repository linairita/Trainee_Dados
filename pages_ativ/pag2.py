import streamlit as st
import pandas as pd

st.title("Adicionar Dados 🎲")

df = st.session_state.df

with st.form("Forms"):
    col1, col2 = st.columns(2)
    with col1:
        choice = st.number_input("Respirações Por Minuto", 0, 100)
        choice = st.number_input("Batimentos por Minuto", 0, 200)
        choice = st.number_input("Temperatura (°C)", 0, 100)   
        choice = st.radio("Consciência:", ["Alerta", "Responsivo com dores", "Confuso", "Verbal", "Não responsivo"])
    with col2:
        number = st.slider("Saturação de Oxigênio no Sangue (%)", 0, 100)
        number = st.slider("Pressão Sanguínea Sistólica", 0, 200)
        st.pills("Escala de Oxigenoterapia", ["Escala 1", "Escala 2"])
        choice = st.radio("Paciente está utilizando suplemento de Oxigênio?", ["Sim", "Não"])
        choice = st.radio("Nível de Risco:", ["Baixo", "Normal", "Médio", "Alto"])

    st.form_submit_button("Adicionar")
