import pandas as pd
import streamlit as st
import plotly_express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title("Aplicación Web de Análisis de Vehículos")

# Descripción de la aplicación
st.markdown("""
Esta aplicación web permite visualizar y analizar datos de anuncios de venta de coches.
Selecciona las opciones a continuación para mostrar un histograma del odómetro o un diagrama de dispersión de precio vs odómetro.
""")

# Crear casillas de verificación para el histograma y el diagrama de dispersión
hist_checkbox = st.checkbox('Mostrar histograma')
disp_checkbox = st.checkbox('Mostrar diagrama de dispersión')

# Si se selecciona la casilla de verificación del histograma
if hist_checkbox:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Si se selecciona la casilla de verificación del diagrama de dispersión
if disp_checkbox:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el diagrama de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)