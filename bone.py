import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px

petCon = pd.read_csv('data/동물위탁관리업.csv')
      ## bar 차트 그리기
st.dataframe( petCon.head() )
st.bar_chart(petCon[['소재지전체주소', '개방서비스명']])