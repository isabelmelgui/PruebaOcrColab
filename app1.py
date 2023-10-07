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
    bytes_data = img_file_buffer2.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro2 == 'Con Filtro':
         cv2_img =cv2.bitwise_not(cv2_img)
    else:
         cv2_img = cv_img
    
        
    img_rgb2 = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text2 =pytesseract.image_to_string(img_rgb2)
    st.write(text2) 

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Escucha las características de la prenda")


tld="es"

def text_to_speech(text2, tld):
    
    tts2 = gTTS(text2,"es", tld, slow=False)
    try:
        my_file_name2 = text2[0:20]
    except:
        my_file_name2 = "audio"
    tts.save(f"temp/{my_file_name2}.mp3")
    return my_file_name2, text2

#display_output_text = st.checkbox("Verifica el texto")

if st.button("Escuchar características"):
    result, output_text2 = text_to_speech(text2, tld)
    audio_file2 = open(f"temp/{result}.mp3", "rb")
    audio_bytes2 = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_byte2s, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)


