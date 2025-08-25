import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Análise: Riscos de Saúde ⚕️")

if 'df' not in st.session_state or st.session_state.df.empty:
    st.warning("Por favor, carregue os dados na página principal primeiro.")
    st.stop()

df = st.session_state.df

mapa_Risk_Level = {1: 'Baixo',
                   2: 'Normal',
                   3: 'Médio',
                   4: 'Alto'
                   }
df['Risk_Level_legenda'] = df['Risk_Level'].map(mapa_Risk_Level)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Registros", value=df.shape[0])
with col2:
    st.metric(label="Batimentos Cardíacos", value=f"{df['Heart_Rate'].mean():.2f} bpm")
with col3:
    st.metric(label="Média de Temperatura Corporal", value=f"{df['Temperature'].mean():.2f} °C")

st.markdown("---")

col1, col2 = st.columns(2)
with col1: 
    st.subheader("Taxa de Respiração")
    fig_hist = px.histogram(
        df,
        x='Respiratory_Rate',
        nbins=30,
        title="Frequência de Respiração (por minuto)",
        labels={'Respiratory_Rate': 'Taxa de Respiração'},
        color_discrete_sequence=['#054f77']
    )
    st.plotly_chart(fig_hist,use_container_width=True)
    st.subheader("Taxa de Batimentos")
    fig_hist = px.histogram(
        df,
        x='Heart_Rate',
        nbins=30,
        title=('Frequência de Batimentos (por minuto)'),
        labels={'Heart_Rate': 'Taxa de Batimentos'},
        color_discrete_sequence=['#6c8ce8']
    )
    st.plotly_chart(fig_hist,use_container_width=True)
with col2:
    st.subheader("Níveis de Risco")
    risk_level_counts = df['Risk_Level_legenda'].value_counts().reset_index()
    risk_level_counts.columns = ['Risk_Level', 'count']
    fig_pie = px.pie(
        risk_level_counts,
        names='Risk_Level',
        values='count',
        title="Proporção de Níveis de Risco",
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    st.subheader("Relação: Temperatura vs. Nível de Risco")
    fig_scatter = px.scatter(
        df,
        x= 'Risk_Level',
        y='Temperature',
        title="Temperatura vs. Nível de Risco",
        labels={'Risk_Level': 'Nível de risco', 'Temperature': 'Temperatura (°C)'},
        color='Risk_Level',
        color_discrete_map={'Risk_Level': '#5391c7', 'Temperature': 'Respiratory_Rate'},
        hover_data=['On_Oxygen', 'Heart_Rate', 'Respiratory_Rate']
    )
    st.plotly_chart(fig_scatter, use_container_width=True)