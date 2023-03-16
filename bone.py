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








