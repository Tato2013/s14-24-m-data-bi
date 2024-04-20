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

# @st.experimental_memo
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data=f.read()
#     return base64.b64encode(data).decode()
# img=get_img_as_base64("../s14-24-m-data-bi/Media/imgia.jpeg")


# page_bg_img =f"""
# <style>
# [data-test_id="stheader"] > div:first_child {{
# background-image:url("data:image/png;base64,{img}");
# background-size: cover;
# background-position: center;
# }}
# </style>
# """
st.set_page_config(page_title="Octanus",
                   page_icon="../s14-24-m-data-bi/Media/logo.png",
                   layout="wide")

color_de_fondo = "#363636"
st.title("OCTANUS ")
st.markdown("_Version 1.0_")
img = Image.open("../s14-24-m-data-bi/Media/logo.png")
imagen = img.resize((700, 150))
st.image(imagen)
st.sidebar.success("select a page above")

st.subheader('Objetivo del proyecto:')
texto = """
            El precio de los combustibles es esencial para la economía argentina, afectando aspectos como el costo de vida, la competitividad empresarial y la estabilidad macroeconómica. Nuestro proyecto de Business Intelligence (BI) busca ofrecer una plataforma completa para analizar y visualizar datos relacionados con los precios de los combustibles en Argentina desde el año 2001 a 2024. Utilizamos datos históricos para proporcionar información y herramientas analíticas a diversos stakeholders, entre ellos empresas energéticas, estaciones de servicio, reguladores gubernamentales, investigadores y ciudadanos. Nuestra plataforma ofrece visualización de tendencias, análisis comparativos, mapas e incluso analisis predictivos para diversas metricas. El objetivo es facilitar la toma de decisiones informadas, identificar oportunidades y riesgos, y comprender mejor los factores que influyen en el mercado de combustibles en Argentina, contribuyendo así al desarrollo de estrategias más eficientes y sostenibles en el sector energético."""
st.write(texto)

# elif seleccion == "ETL":
#     st.subheader('Extracción inicial de datos:')
#     texto = """Se obtienen los datos del Ministerio de Energia de Argentina para los precios de combustibles , asi cómo el histórico de la cotizaión del dólar en Argentina :
#             """
#     st.write(texto)
    
#     with st.expander('Datos sin procesar'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/Datos Challenge limpios.csv")
#         st.write(df)
  
#     st.subheader('Transformación de los datos:')
#     texto ="""Creación de tablas y relaciones:
#               Mediante cambios en la estructura de los datos, se definieron distintas tablas en las que dividimos los registros, para su escalabilidad.
#               De esta manera la base de datos no solo es más eficiente y optimiza el rendimiento, sino que permite hacer análisis más detallados de algunos puntos importantes, como las ventas por productos."""
#     st.write(texto)
    
#     with st.expander('Listado de empresas'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-de-empresas.csv")
#         st.write(df)
        
     
#     with st.expander('Listado de productos'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-de-productos.csv")
#         st.write(df)

#     with st.expander('Listado de empresas bandera'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/listado-empresas-bandera.csv")
#         st.write(df)

#     with st.expander('Valor dolar oficial'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/valor_dolar_oficial_normalizado.csv")
#         st.write(df)

#     with st.expander('Valor dolar blue'):
#         df = pd.read_csv("../s14-24-m-data-bi/base_de_datos/archivos_csv/dolar_blue_normalizado.csv")
#         st.write(df)
        
#     @st.cache_data
#     def load_data(file):
#         data=pd.read_csv(file)
#         return data
    
#     uploaded_file= st.file_uploader("Cargue archivo csv")
#     df = load_data(uploaded_file)
#     st.write(df)

#     st.subheader('Estructura final de nuestra base de datos:')
#     texto ="""Relaciones entre las distintas tablas:"""
#     st.write(texto)    

#     # with st.expander('Relaciones'):
#     img = Image.open("../s14-24-m-data-bi/Media/imggeneral.jpeg")
#     imagen = img.resize((800, 400))
#     st.image(imagen)    

# elif seleccion == "Análisis de datos":

#     st.write("## Análisis de datos:")
#     st.write("A través de Power BI realizamos un análisis de los datos del precio de combustible, que se pueden consultar de manera interactiva en el siguiente dashboard:")
    
#     # with st.expander('Dashboard'):
#     img = Image.open("../s14-24-m-data-bi\Media\PowerBI_Inicio.jpg")
#     imagen = img.resize((800, 400))
#     st.image(imagen)    

#     # st.write("<iframe width='1000' height='600' src='https://app.powerbi.com/view?r=eyJrIjoiYmMxMWIwMWYtNDFjMy00NDIyLTg3ODQtMzM5MTJiZDk3M2VhIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9' style='display:block;margin:auto;'></iframe>", unsafe_allow_html=True)

# elif seleccion == "Predicciones":
#     st.write("Oráculo de Octanus")
#     img = Image.open("../s14-24-m-data-bi\Media\oraculo.jpeg")
#     imagen = img.resize((800, 400))
#     st.image(imagen)  
    

   