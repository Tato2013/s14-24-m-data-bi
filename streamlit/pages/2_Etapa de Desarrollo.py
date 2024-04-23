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
texto = """Se obtienen los datos del Ministerio de Energia de la República Argentina para los precios de combustibles, el cual se usó para entrenar el modelo predictivo. Tambien se usó la data del Challenge, el cual se basa en los datos del ministerio y que sirvió de insumo para el dashboard:
        """
st.write(texto)

with st.expander('Datos sin procesar Ministero de Energia de Argentina'):
    df = pd.read_csv("../base_de_datos/archivos_csv/Datos Challenge sucios.csv")
    st.write(df)
    
st.subheader('Transformación de los datos:')

st.subheader('## Limpieza de datos:')
texto = """Se realizó la revisión y limpieza de los dataset segun se muestra en el link siguiente:
"""
st.write(texto)
st.markdown("[S14_24_Dataset_Challenge_Limpieza_y_Normalizado.ipynb](https://colab.research.google.com/drive/1sKhEWzbkkvxeY-fy5MTZJ74Of6aM-9Sd?usp=sharing)")

st.subheader('## Creación de tablas y relaciones:')
texto ="""
    Mediante cambios en la estructura de los datos, se definieron distintas tablas en las que dividimos los registros, para su escalabilidad.
    De esta manera la base de datos no solo es más eficiente y optimiza el rendimiento, sino que permite hacer análisis más detallados de algunos puntos importantes, como las ventas por productos."""
st.write(texto)

with st.expander('Precio'):
    df = pd.read_csv("../base_de_datos/archivos_csv/primeros_1000_registros.csv")
    st.write(df)
    
with st.expander('Empresas'):
    df = pd.read_csv("../base_de_datos/archivos_csv/listado-de-empresas.csv")
    st.write(df)

with st.expander('Empresas bandera'):
    df = pd.read_csv("../base_de_datos/archivos_csv/listado-empresas-bandera.csv")
    st.write(df)
    
with st.expander('Productos'):
    df = pd.read_csv("../base_de_datos/archivos_csv/listado-de-productos.csv")
    st.write(df)
    
st.subheader('Creación de tablas complementarias :')
texto ="""Tablas de precio histórico del dolar en Argentina:
    Creadas a partir de la investigación de la cotización del dolar en el periodo del análisis."""
st.write(texto)

with st.expander('Valor dolar oficial'):
    df = pd.read_csv("../base_de_datos/archivos_csv/valor_dolar_oficial_normalizado.csv")
    st.write(df)

with st.expander('Valor dolar blue'):
    df = pd.read_csv("../base_de_datos/archivos_csv/dolar_blue_normalizado.csv")
    st.write(df)


st.subheader('Estructura final de nuestra base de datos:')
texto ="""Relaciones entre las distintas tablas:"""
st.write(texto)    

# with st.expander('Relaciones'):
img = Image.open("../streamlit/Media/tablas y relaciones.png")
imagen = img.resize((800, 400))
st.image(imagen)    

