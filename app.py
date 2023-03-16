# # streamlit 라이브러리 호출
# import streamlit as st
# from PIL import Image
# # import graph.py

# st.title("팻밀리")
# st.subheader("반려견 행복지도")

# # image = Image.open(+'/PetHospital.png')
# # st.image(image, caption='동물병원')

# st.image(f"imagefiles/PetHospital.png", caption='동물병원')



import pandas as pd
import numpy as np


seoul_pet_hospital = pd.read_csv("https://raw.githubusercontent.com/whataLIN/sample_rp/main/data/PetHospital.csv")