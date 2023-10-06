import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Reconocimiento óptico de Caracteres")

img_file_buffer2 = st.file_uploader("Choose a jpg file")

with st.sidebar:
      filtro2 = st.radio("Aplicar Filtro",('Con Filtro', 'Sin Filtro'))


if img_file_buffer2 is not None:
    # To read image file buffer with OpenCV:
    bytes_data2 = img_file_buffer2.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro2 == 'Con Filtro':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img = cv_img
    
        
    img_rgb2 = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb2)
    st.write(text) 


    


