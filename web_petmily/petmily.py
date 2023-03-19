import plotly.express as px
import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import re
import copy

st.write(
    """
    ## 🐶 팻밀리
    #### 반려견을 기르기 위한 최적의 인프라 환경 조사 시각화
    ---
    """
)

address = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구","중랑구"]
st.sidebar.title('자치구를 선택해주세요! 👇')
selected_region = st.sidebar.selectbox("자치구 선택", address
)


# 서울시 동물병원 파일 불러오기
seoul_pet_hospital = pd.read_csv('web_petmily/서울시_동물병원.csv', encoding = 'cp949')
# 서울시 애견미용업장 파일 불러오기
seoul_pet_beauty = pd.read_csv('web_petmily/서울시 애견미용업장.csv')
# 서울시 애견위탁관리 파일 불러오기
seoul_pet_con = pd.read_csv('web_petmily/동물위탁관리업.csv')
# 서울시 주요 공원 현황 파일 불러오기
seoul_park = pd.read_csv('web_petmily/서울시 주요 공원현황.csv', encoding = 'cp949')
# 반려동물 유무 비율 보유 파일 불러오기
seoul_pet_own = pd.read_csv('web_petmily/반려동물+유무+및+취득+경로_20230314161547.csv')


#@title 서울시 동물병원 파일 불러오기
sph = seoul_pet_hospital.copy()
sph = sph.dropna(how='all')

#@title 필요없는 컬럼들 제거
cols1 = ["총직원수", "인허가일자", "인허가취소일자","상세영업상태코드","최종수정시점","데이터갱신구분","업태구분명","데이터갱신일자", "상세업무구분명", "개방자치단체코드","관리번호","영업상태구분코드","폐업일자",
         "휴업시작일자","소재지면적","소재지우편번호", "상세영업상태명","휴업종료일자", "재개업일자","개방서비스아이디","권리주체일련번호","업무구분명"]

for col in cols1:
    del sph[col]

#@title '소재지전체주소' 컬럼에서 '서울'을 포함한 데이터만 필터링
sph = sph[sph['소재지전체주소'].str.contains('서울', na=False)]

sph_list = ["강서구",
            "양천구",
            "구로구",
            "금천구",
            "영등포구",
            "동작구",
            "관악구",
            "서초구",
            "강남구",
            "송파구",
            "강동구",
            "마포구",
            "은평구",
            "서대문구",
            "종로구",
            "중구",
            "용산구",
            "성북구",
            "성동구",
            "동대문구",
            "광진구",
            "중랑구",
            "노원구",
            "도봉구",
            "강북구"
]

pattern = '|'.join(sph_list)
sph['소재지전체주소'] = sph['소재지전체주소'].str.extract(f'({pattern})', flags=re.IGNORECASE)

sph_gu=(sph.groupby(sph['소재지전체주소']).count())[["사업장명"]]

sph_sort = sph_gu.sort_values(by=['사업장명'], ascending=False)


# 소재지 전체주소 별 사업장 수 계산
sph_sort2 = sph.groupby('소재지전체주소').count().reset_index()
sph_sort3 = sph_sort2.sort_values(by=['사업장명'], ascending=False)


# 동물병원 수 plotly 차트
fig_hos = px.bar(sph_sort, x=sph_sort.index, y='사업장명', color='사업장명',
             color_continuous_scale='Blues',
             labels={'x': '자치구', 'y': '동물병원 수'},
             height=400)
fig_hos.update_layout(
    title='서울시 자치구별 동물병원 수',
    showlegend=False,
    xaxis_title='',
    yaxis_title='동물병원 수',
    font=dict(size=3),
)
fig_hos.update_xaxes(tickfont_size=7,tickangle=45)


# # 동물 병원 수 Altair 차트 
# bar_chart = alt.Chart(sph_sort3).mark_bar(
# ).encode(
#     x=alt.X('소재지전체주소',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
#     y=alt.Y('사업장명',axis=alt.Axis(title=''),sort='-y'),
#     color=alt.Color('소재지전체주소', scale=alt.Scale(scheme='darkblue'), legend=None)
# ).properties(
# )


#@title 서울시 애견미용업장 파일 불러오기
# 번호, 구분, 업체명, 소재지

#@title 서울시 애견 미용업장 파일 복사
spb = seoul_pet_beauty.copy()

# 인허가 정보 컬럼들 제거
cols1 = ["번호", "인허가 정보", "이전인허가정보"]

for col in cols1:
    del spb[col]

pattern = '|'.join(sph_list)

spb['소재지'] = spb['소재지'].str.extract(f'({pattern})', flags=re.IGNORECASE)
spb2 = spb.groupby(spb["소재지"]).count()[["업체명"]]
spb_sort = spb2.sort_values(by=['업체명'], ascending=False)

fig_beauty = px.bar(spb_sort, x=spb_sort.index, y='업체명', color='업체명',
             color_continuous_scale='plotly3',
             labels={'x': '자치구', 'y': '애견 미용실 수'},
             height=400)
fig_beauty.update_layout(
    title='서울시 자치구별 애견 미용실 수',
     showlegend=False,
    xaxis_title='',
    yaxis_title='애견 미용실 수',
    font=dict(size=3),
)
fig_beauty.update_xaxes(tickfont_size=7,tickangle=45)

# # 애견 미용 Altair 차트
# bar_chart2 = alt.Chart(spb_sort).mark_bar(
# ).encode(
#     x=alt.X('소재지',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
#     y=alt.Y('업체명',axis=alt.Axis(title=''), sort='-y'),
#     color=alt.Color('소재지', scale=alt.Scale(scheme='pinkyellowgreen'), legend=None)
# ).properties(
# )




# 반려동물 CSV 파일 읽어오기
pet_have = pd.read_csv('web_petmily/반려동물+유무+및+취득+경로_20230314161547.csv')
# 특정열에 특정값을 가진 행 추출하기
pet_have2 = pet_have[pet_have['구분별(1)'].str.contains("지역소분류")]
# 추출된 데이터를 새로운 CSV 파일로 저장하기
pet_have2.to_csv('반려동물 유무.csv', index=False)


pet_have_dict = dict(zip(pet_have2['구분별(2)'], pet_have2['2021']))
pet_have_dict2 = copy.deepcopy(pet_have_dict)
pet_have_dict_sorted_items = sorted(pet_have_dict2.items(), key=lambda x: x[1], reverse=True)
pet_have_dict_sorted = dict(pet_have_dict_sorted_items)

pet_have_df = pd.DataFrame(pet_have_dict_sorted.items(), columns=['gu', 'data'])
pet_have_df['data'] = pet_have_df['data'].astype('float')
pet_have_df.sort_values('data', inplace=True, ascending=False)


fig_tf = px.bar(pet_have_df, x='gu', y='data', color='data',
             color_continuous_scale='purp',
             labels={'gu': '자치구', 'data': '반려동물 보유 비율'},
             height=400, width=450)
fig_tf.update_layout(
    showlegend=False,
    title='서울시 자치구별 주민 반려동물 보유 비율',
    xaxis_title='',
    yaxis_title='주민 반려동물 보유 비율(%)',
    font=dict(size=3),
)
fig_tf.update_xaxes(tickfont_size=7,tickangle=45)

# 반려동물 보유 비율 Altair 차트
# bar_chart3 = alt.Chart(pet_have_df).mark_bar(
# ).encode(
#     x=alt.X('gu',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
#     y=alt.Y('data',axis=alt.Axis(title=''),sort='-y'),
#     color=alt.Color('gu', scale=alt.Scale(scheme='darkgold'), legend=None)
# ).properties(
# )



# 서울시 애견위탁관리 파일 불러오기
# 번호, 구분(위탁관리 포함된 문자만), 업체명, 소재지
spc = seoul_pet_con.groupby([seoul_pet_con["개방서비스명"],seoul_pet_con["소재지전체주소"]])
spc2 = spc[["소재지전체주소"]].count().rename(columns={"소재지전체주소": "개수"})


dict1 = spc2.iloc[1:].loc[:,'개수'].reset_index(level=0, drop=True).to_dict()
dict2 = copy.deepcopy(dict1)
dict2_keys_list = list(dict2.keys())
dict2_values_list = list(dict2.values())
dict2_keys_list2 = [x + "구" for x in dict2_keys_list]
dict2_keys_list3 = [x.replace("서울특별시", "") for x in dict2_keys_list2]
done_dict = dict(zip(dict2_keys_list3, dict2_values_list))

# 정렬
sorted_items = sorted(done_dict.items(), key=lambda x: x[1], reverse=True)
sorted_done_dict = dict(sorted_items)

spc_gu = pd.DataFrame(sorted_done_dict.items(), columns=['gu', 'data'])
spc_gu['data'] = spc_gu['data'].astype('float')
spc_gu.sort_values('data', inplace=True, ascending=False)

# 반려동물 위탁 업체 수
fig_con = px.bar(spc_gu, x='gu', y='data', color='data',
             color_continuous_scale='Brwnyl',
             labels={'gu': '자치구', 'data': '반려동물 위탁 업체 수'},
             height=400, width=450)
fig_con.update_layout(
    title='서울시 자치구별 반려동물 위탁 업체 수',
    xaxis_title='',
    yaxis_title='반려동물 위탁 업체 수',
    font=dict(size=3),
    showlegend=False,
)
fig_con.update_xaxes(tickfont_size=7,tickangle=45)

# 반려동물 위탁 업체 수 Altair 차트
# bar_chart3 = alt.Chart(spc_gu).mark_bar(
# ).encode(
#     x=alt.X('gu',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
#     y=alt.Y('data',axis=alt.Axis(title=''),sort='-y'),
#     color=alt.Color('gu', scale=alt.Scale(scheme='darkgold'), legend=None)
# ).properties(
# )


# 서울시 주요 공원 현황 파일 불러오기
# 연번, 공원명, 공원개요("맑은 공기"), 면적, 주요 시설, 주요 식물, 공원주소, 관리부서, 전화번호, 바로가기

def change_addr(index, new_addr):
  park_info.loc[index, '공원주소'] = new_addr

park_info=seoul_park[["연번","공원명","공원주소"]].copy()

seoul_not_in_addr = park_info[park_info['공원주소'].apply(lambda x: '서울특별시' not in x)]

change_addr(129, "서울특별시 노원구 공릉2동 산 82-2")
change_addr(131, "서울특별시 중구 서울로7017")
park_info = park_info.drop(2)
park_info.reset_index(inplace=True)

for idx, addr in enumerate(park_info["공원주소"]):
  park_info['공원주소'][idx]=list(str(addr).split(" "))[1]

park_info['공원주소'] = park_info['공원주소'].apply(lambda x: ' '.join(x))

parksg_gu=(park_info.groupby(park_info['공원주소']).count())[["공원명"]].sort_values(by='공원명', ascending=False)

parksg_gu = parksg_gu.rename(columns={'공원명': '공원 수', '공원주소':'자치구'})

fig_park = px.bar(parksg_gu, x=parksg_gu.index, y='공원 수', color='공원 수',
             color_continuous_scale='Greens',
             labels={'x': '자치구', 'y': '공원 수'},
             height=400)
fig_park.update_layout(
    title='서울시 자치구별 공원 수',
    xaxis_title='',
    yaxis_title='공원 수',
    font=dict(size=3),
    showlegend=False,
)
fig_park.update_xaxes(tickfont_size=7,tickangle=45)


# 종합 순위 데이터 가공
#@title 동물병원순위
sph_sort["동물병원순위"] = sph_sort['사업장명'].rank(method='min', ascending=True)


#@title 동물미용업체순위
spb_sort["동물미용업체순위"] = spb_sort['업체명'].rank(method='min', ascending=True)


#@title 공원순위
parks_rank=parksg_gu.copy()
parks_rank['공원순위'] = parks_rank['공원 수'].rank(method='min', ascending=True)


#@title 반려동물 보유 비율 순위
pet_have_df['보유 비율 순위'] = pet_have_df['data'].rank(method='min', ascending=True)
pet_have_df_rank = pet_have_df[['gu', '보유 비율 순위']]
pet_have_df_rank = pet_have_df_rank.set_index("gu")


#@title 동물위탁순위
spc_gu['위탁 업체 수'] = spc_gu['data'].rank(method='min', ascending=True)
pet_cs = spc_gu[['gu', '위탁 업체 수']]
pet_cs2=pet_cs.set_index("gu")


# 데이터 프레임 합성
address = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구","중랑구"]
sph_sort_index = sph_sort.sort_index(ascending=True)
spb_sort_index = spb_sort.sort_index(ascending=True)

parks_rank2= parks_rank[['공원순위']]
parks_rank2_index = parks_rank2.sort_index(ascending=True)

pet_cs2_index = pet_cs2.sort_index(ascending=True)
pet_have_df_rank_index = pet_have_df_rank.sort_index(ascending=True)

sph_sort_index = sph_sort.sort_index(ascending=True)
spb_sort_index = spb_sort.sort_index(ascending=True)

spb_sort_tomerge = spb_sort_index.assign(C=address)
spb_sort_tomerge2=spb_sort_tomerge.set_index("C")

sph_sort_tomerge = sph_sort_index.assign(C=address)
sph_sort_tomerge2=sph_sort_tomerge.set_index("C")

pet_have_tomerge = pet_have_df_rank_index.assign(C=address)
pet_have_tomerge2=pet_have_tomerge.set_index("C")

pet_cs_tomerge = pet_cs2_index.assign(C=address)
pet_cs_tomerge2=pet_cs_tomerge.set_index("C")

parks_tomerge = parks_rank2_index.assign(C=address)
parks_tomerge2=parks_tomerge.set_index("C")

concatenated_df = pd.concat([pet_cs_tomerge2, pet_have_tomerge2, parks_tomerge2, spb_sort_tomerge2,sph_sort_tomerge2], axis=1)

result = concatenated_df[['동물병원순위', '동물미용업체순위', '위탁 업체 수',"보유 비율 순위","공원순위"]]
result["합계"] = result.sum(axis=1)
result1 = result["합계"].sort_values(ascending=False)

#@title 서울시 자치구별 종합 막대 그래프

result1 = result["합계"].sort_values(ascending=False)
result1_df = result1.to_frame(name='합계').reset_index().rename(columns={'index': '자치구'})

fig_syn = px.bar(result1_df, x='C', y='합계', color='합계',
             color_continuous_scale='greys',
             labels={'C': '자치구', '합계': '종합순위'},
             height=400)
fig_syn.update_layout(
    title='서울시 자치구별 반려동물 편의지수 종합순위',
    xaxis_title='',
    yaxis_title='편의지수 종합순위',
    font=dict(size=3),
    showlegend=False,
)
fig_syn.update_xaxes(tickfont_size=7,tickangle=45)



result2 = result[['동물병원순위', '동물미용업체순위', '위탁 업체 수',"보유 비율 순위","공원순위"]]

# 오각형 방사형 차트 생성 및 출력

# 데이터 프레임 생성
df = pd.DataFrame(result2, index=address)
# 사이드바에서 자치구 선택
# 선택한 자치구에 해당하는 데이터 추출
selected_data = df.loc[selected_region]

# 방사형 차트 생성
fig_radar = px.line_polar(
    r=selected_data.values,
    theta=selected_data.index,
    line_close=True,
)
fig_radar.update_traces(fill='toself')

# 차트 레이아웃 설정
fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 30]),
        angularaxis=dict(direction="clockwise"),
    ),
    showlegend=False,
    title=f"{selected_region} 종합 시각화 차트"
)
# 차트 출력
st.plotly_chart(fig_radar, theme="streamlit", use_container_width=True)



col1,col2 = st.columns([1,1])
# 공간을 1:1 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

with col1 :
  # column 1 에 담을 내용
  st.plotly_chart(fig_hos, theme="streamlit", use_container_width=True)
  st.info('자치구별 동물 병원수 입니다.', icon="ℹ️")
  
  st.plotly_chart(fig_beauty, theme="streamlit", use_container_width=True)
  st.info('자치구별 동물 미용업체수 입니다.', icon="ℹ️")

  st.plotly_chart(fig_tf, theme="streamlit")
  st.info('자치구별 반려동물 보유비율입니다.', icon="ℹ️")



with col2 :
  # column 2 에 담을 내용
  st.plotly_chart(fig_con, theme="streamlit")
  st.info('자치구별 동물 위탁시설 수 입니다.', icon="ℹ️")
  
  st.plotly_chart(fig_park, theme="streamlit", use_container_width=True)
  st.info('자치구별 공원 시설 수 입니다.', icon="ℹ️")

  st.plotly_chart(fig_syn, theme="streamlit", use_container_width=True)
  st.info('자치구별 종합 순위 입니다.', icon="ℹ️")
  
# 데이터 출처 :

