import streamlit as st

st.title("Dashboard de insights")

df = st.session_state.df

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Registros", value=df.shape[0])
with col2:
    st.metric(label="Média de Idade", value=f"{df['Age'].mean():.2f} anos")
with col3:
    st.metric(label="Média de Tempo de Tela", value=f"{df['Avg_Daily_Screen_Time_hr'].mean():.2f} horas")

st.markdown("---")
