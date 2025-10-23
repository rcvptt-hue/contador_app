# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:52:45 2025

@author: rccorreall
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Formulario de Evaluación", page_icon="📊", layout="centered")

# Logo más pequeño
st.image("logo.png", width=300)

st.markdown("<h2 style='text-align:center;'>Evaluación de Proyectos</h2>", unsafe_allow_html=True)
st.markdown("---")

# Crear archivo CSV si no existe
csv_file = "respuestas.csv"
if not os.path.exists(csv_file):
    df_init = pd.DataFrame(columns=["timestamp", "pregunta1", "pregunta2", "pregunta3", "pregunta4", "pregunta5"])
    df_init.to_csv(csv_file, index=False)

# Cargar respuestas
df = pd.read_csv(csv_file)

# Mostrar contador total de respuestas
contador = len(df)
st.markdown(f"<h3 style='text-align:center;'>Total de respuestas recibidas: {contador}</h3>", unsafe_allow_html=True)
st.markdown("---")

# Formulario
st.subheader("📝 Responde las siguientes preguntas")

with st.form("formulario"):
    p1 = st.selectbox("1️⃣ ¿Qué tan clara fue la presentación del proyecto?", [1, 2, 3, 4, 5])
    p2 = st.selectbox("2️⃣ ¿Qué tan innovadora consideras la propuesta?", [1, 2, 3, 4, 5])
    p3 = st.selectbox("3️⃣ ¿Qué tan viable es la implementación?", [1, 2, 3, 4, 5])
    p4 = st.selectbox("4️⃣ ¿Qué tan sustentable es el proyecto a largo plazo?", [1, 2, 3, 4, 5])
    p5 = st.selectbox("5️⃣ ¿Qué tanto potencial de crecimiento tiene?", [1, 2, 3, 4, 5])

    submitted = st.form_submit_button("Enviar respuesta ✅")

    if submitted:
        nueva_fila = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "pregunta1": [p1],
            "pregunta2": [p2],
            "pregunta3": [p3],
            "pregunta4": [p4],
            "pregunta5": [p5],
        })
        nueva_fila.to_csv(csv_file, mode="a", header=False, index=False)
        st.success("✅ ¡Respuesta enviada con éxito!")
        st.balloons()
        st.rerun()
