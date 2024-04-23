import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt
import logging
logger = logging.getLogger('cmdstanpy')
logger.addHandler(logging.NullHandler())
logger.propagate=False
logger.setLevel(logging.CRITICAL)
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Octanus",
                   page_icon="../streamlit/Media/logo.png",
                   layout="wide")

st.title("OCTANUS ")
st.markdown("_Version 1.0_")
img = Image.open("../streamlit/Media/logo.png")
imagen = img.resize((700, 150))
st.image(imagen)


st.subheader('Objetivo del proyecto:')
texto = """
El precio de los combustibles es esencial para la economía argentina, afectando aspectos como el costo de vida, la competitividad empresarial y la estabilidad macroeconómica. Nuestro proyecto de Business Intelligence (BI) busca ofrecer una plataforma completa para analizar y visualizar datos relacionados con los precios de los combustibles en Argentina desde el año 2001 a 2024. Utilizamos datos históricos para proporcionar información y herramientas analíticas a diversos stakeholders, entre ellos empresas energéticas, estaciones de servicio, reguladores gubernamentales, investigadores y ciudadanos. Nuestra plataforma ofrece visualización de tendencias, análisis comparativos, mapas e incluso analisis predictivos para diversas metricas. El objetivo es facilitar la toma de decisiones informadas, identificar oportunidades y riesgos, y comprender mejor los factores que influyen en el mercado de combustibles en Argentina, contribuyendo así al desarrollo de estrategias más eficientes y sostenibles en el sector energético."""
st.write(texto)