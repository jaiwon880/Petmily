# streamlit 라이브러리 호출
import streamlit as st
import graph.py

st.title("팻밀리")

st.subheader("반려견 행복지도")

st.write(graph.seoulPetHospital())


#==========================================================

st.sidebar.title('시간 순삭 유튜브 추천👇')
add_selectbox = st.sidebar.selectbox("주인장 추천 채널",
 ["지식한입", "ITSub잇섭", "느낌적인느낌","호갱구조대", "너 진짜 똑독하다", "슈카월드"])

values = st.sidebar.slider('추천 채널 만족도를 평가', 1, 5)
st.sidebar.write('평가 점수:', values)


col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

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
petCon

seoul_pet_con = pd.read_csv("data/동물위탁관리업.csv")
seoul_pet_con
3:41
spc = seoul_pet_con.groupby([seoul_pet_con["개방서비스명"],seoul_pet_con["소재지전체주소"]])
spc
spc2 = spc[["소재지전체주소"]].count().rename(columns={"소재지전체주소": "개수"})
spc2
dict1 = spc2.iloc[1:].loc[:,'개수'].reset_index(level=0, drop=True).to_dict()
dict1
import copy
dict2 = copy.deepcopy(dict1)
dict2
dict2_keys_list = list(dict2.keys())
print(dict2_keys_list)
dict2_values_list = list(dict2.values())
print(dict2_values_list)
dict2_keys_list2 = [x + "구" for x in dict2_keys_list]
dict2_keys_list2
dict2_keys_list3 = [x.replace("서울특별시", "") for x in dict2_keys_list2]
dict2_keys_list3
done_dict = dict(zip(dict2_keys_list3, dict2_values_list))
print(done_dict)
done_dict
sorted_items = sorted(done_dict.items(), key=lambda x: x[1], reverse=True)
sorted_done_dict = dict(sorted_items)
print(sorted_done_dict)
spc_gu = pd.DataFrame(sorted_done_dict.items(), columns=['구', 'data'])
spc_gu['data'] = spc_gu['data'].astype('float')
spc_gu.sort_values('data', inplace=True, ascending=False)
# 그라데이션 색상을 위한 컬러 맵 생성
cmap = plt.get_cmap('coolwarm')
# 데이터프레임에서 값을 가져와서 바차트를 그립니다.
fig, ax = plt.subplots(figsize = (20, 10))
# bars = ax.bar(list(sorted_dict2.keys())[::-1], list(sorted_dict2.values())[::-1], align='center')
bars = ax.bar(spc_gu.구, spc_gu.data, align='center')
# 그라데이션 색상 적용
for i, bar in enumerate(bars):
    bar.set_color(cmap(i / len(list(sorted_done_dict.keys()))))
# x축 레이블 설정
plt.xticks(rotation = 45, fontsize = 15)
# 그래프 타이틀 설정
plt.title('서울시 자치구별 주민 반려동물 보유 비율')
# 그래프 출력
plt.show()

with col1 :
  # column 1 에 담을 내용
  st.markdown("**나에게 :blue[가장 도움이 될 것 같은] 유튜브**")

  st.image("https://user-images.githubusercontent.com/71927533/221650828-c1a86b95-99ac-4a85-a4cc-e398eaf2865f.jpg")
  st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon="ℹ️")
  
  # Text Area
  message = st.text_area("소개해 드린 추천 채널의 느낀점을 입력해 주세요", "이곳에 입력하세요.")
  if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)

  st.write(
    """
    > 출처: [빵형의 개발도상국](https://www.youtube.com/@bbanghyong/), [노마드 코더](https://www.youtube.com/@nomadcoders)
    
    """)


with col2 :
  # column 2 에 담을 내용
  st.markdown("**:red[남]이보면 좋을 것 같은 유튜브**")
  st.image("https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg")
  st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon="ℹ️")
  



