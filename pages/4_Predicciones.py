import streamlit as st
import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt


st.title("Predicciones")



st.write("Oráculo de Octanus")
img = Image.open("../s14-24-m-data-bi\Media\oraculo.jpeg")
imagen = img.resize((800, 400))
st.image(imagen)  