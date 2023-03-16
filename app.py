# streamlit 라이브러리 호출
import streamlit as st
from PIL import Image
# import graph.py

st.title("팻밀리")

st.subheader("반려견 행복지도")

image = Image.open(image/'서울동물병원.jpg')

st.image(image, caption='동물병원')

