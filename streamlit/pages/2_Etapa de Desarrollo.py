import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt
import base64 
import logging
logger = logging.getLogger('cmdstanpy')
logger.addHandler(logging.NullHandler())
logger.propagate=False
logger.setLevel(logging.CRITICAL)
import warnings
warnings.filterwarnings('ignore')

st.title("ETL")



st.subheader('Extracción inicial de datos:')
texto = """Se obtienen los datos del Ministerio de Energia de Argentina para los precios de combustibles , asi cómo el histórico de la cotizaión del dólar en Argentina :
        """
st.write(texto)

with st.expander('Datos sin procesar'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/Datos Challenge limpios.csv")
    st.write(df)

st.subheader('Transformación de los datos:')
texto ="""Creación de tablas y relaciones:
    Mediante cambios en la estructura de los datos, se definieron distintas tablas en las que dividimos los registros, para su escalabilidad.
    De esta manera la base de datos no solo es más eficiente y optimiza el rendimiento, sino que permite hacer análisis más detallados de algunos puntos importantes, como las ventas por productos."""
st.write(texto)

with st.expander('Listado de empresas'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-de-empresas.csv")
    st.write(df)


with st.expander('Listado de productos'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-de-productos.csv")
    st.write(df)

with st.expander('Listado de empresas bandera'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-empresas-bandera.csv")
    st.write(df)

with st.expander('Valor dolar oficial'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/valor_dolar_oficial_normalizado.csv")
    st.write(df)

with st.expander('Valor dolar blue'):
    df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/dolar_blue_normalizado.csv")
    st.write(df)


st.subheader('Estructura final de nuestra base de datos:')
texto ="""Relaciones entre las distintas tablas:"""
st.write(texto)    

# with st.expander('Relaciones'):
img = Image.open("../s14-24-m-data-bi/Media/imggeneral.jpeg")
imagen = img.resize((800, 400))
st.image(imagen)    

