# streamlit 라이브러리 호출
import streamlit as st
from PIL import Image
# import graph.py

st.title("팻밀리")
st.subheader("반려견 행복지도")

image = Image.open(imagefiles/'PetHospital.png')
st.image(image, caption='동물병원')

