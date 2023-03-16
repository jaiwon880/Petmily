# import plotly.express as px
import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import re
import copy
# import plotly.graph_objects as go
# import plotly.figure_factory as ff

st.write(
    """
    ## 🐶 팻밀리
    ---
    """
)

gu_dict = {
          "양천구":'https://user-images.githubusercontent.com/126433780/225597044-dce9aa85-d5f0-4fd2-aa74-1df2a9c5f800.png',
          "구로구":'https://user-images.githubusercontent.com/102681611/225593175-da161582-efac-4ce2-9b4b-baec38bbe975.png',
          "금천구":'https://user-images.githubusercontent.com/102681611/225593189-c19a75f6-422f-4d61-a32d-dd27a53fb363.png',
          "영등포구":'https://user-images.githubusercontent.com/126433780/225597045-30d52d72-756b-4610-ab49-296226fc9896.png',
          "동작구":'https://user-images.githubusercontent.com/126433780/225597053-153eff9f-d68e-482b-a927-f43a2c49f548.png',
          "관악구":'https://user-images.githubusercontent.com/102681611/225593571-f1d70f63-ba65-4caf-9630-6529473f3ba2.png',
          "강남구":'https://user-images.githubusercontent.com/102681611/225593391-7293582f-497d-456d-91e0-f67ba4725dd0.png',
          "송파구":'https://user-images.githubusercontent.com/126433780/225597041-40132bf2-71d8-4fb4-a811-914799695761.png',
          "강동구":'https://user-images.githubusercontent.com/102681611/225593451-d53bb67e-ee80-4524-a0a5-e6328cbb6cdf.png',
          "마포구":'https://user-images.githubusercontent.com/126433780/225597056-24513e20-180d-4317-9632-0eca1a17e9ef.png',
          "은평구":'https://user-images.githubusercontent.com/126433780/225597044-dce9aa85-d5f0-4fd2-aa74-1df2a9c5f800.png',
          "서대문구":'https://user-images.githubusercontent.com/126433780/225597058-65f252b1-7163-4965-ab08-ebe814c22962.png',
          "서초구":'https://user-images.githubusercontent.com/126433780/225597062-6f4dacfb-7239-4486-bdab-c44f66ee8127.png',
          "중구":'https://user-images.githubusercontent.com/126433780/225595139-66437a9c-b19f-4ef1-9668-96f3dd25180e.png',
          "용산구":'https://user-images.githubusercontent.com/126433780/225595152-55f7eb4d-53fd-4cd7-b8ac-3d02a7527aff.png',
          "성북구":'https://user-images.githubusercontent.com/126433780/225597038-7a0b1988-0cab-46e0-88d8-6fba4bd70283.png',
          "성동구":'https://user-images.githubusercontent.com/126433780/225597032-1e412772-2abb-4505-8568-92855eae1ff4.png',
          "강서구":'https://user-images.githubusercontent.com/102681611/225593510-12c927fa-4aed-4548-b5a8-b65e80ebf7bd.png',
          "광진구":'https://user-images.githubusercontent.com/102681611/225593153-6192fbec-b2cd-49b4-a7c9-504e85cb00c3.png',
          "중랑구":'https://user-images.githubusercontent.com/126433780/225595146-e82a0c58-ef46-46b2-b23b-23555ffb7648.png',
          "노원구":'https://user-images.githubusercontent.com/102681611/225594115-6594e617-6d97-4bd6-9b6d-b34a68a2f9df.png',
          "도봉구":'https://user-images.githubusercontent.com/102681611/225594214-ef04e6c6-c026-4b80-89b9-1635f9d306e9.png',
          "강북구":'https://user-images.githubusercontent.com/102681611/225593468-a0255c87-c861-4716-8774-818d305fcca1.png',
"동대문구":'https://user-images.githubusercontent.com/126433780/225597051-414a4745-ad14-48a8-badc-e75fd20ca4e5.png'}

st.sidebar.title('자치구를 선택해주세요! 👇')
choice = st.sidebar.selectbox("자치구 선택",
["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구","중랑구"]
)
st.image(gu_dict[choice], use_column_width=True)



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


# 알테어 바 차트 생성
bar_chart = alt.Chart(sph_sort3).mark_bar(
).encode(
    x=alt.X('소재지전체주소',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
    y=alt.Y('사업장명',axis=alt.Axis(title=''),sort='-y'),
    color=alt.Color('소재지전체주소', scale=alt.Scale(scheme='darkblue'), legend=None)
).properties(
)


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



# 소재지 전체주소 별 사업장 수 계산
sph_sort2 = sph.groupby('소재지전체주소').count().reset_index()
sph_sort3 = sph_sort2.sort_values(by=['사업장명'], ascending=False)

spb2 = spb.groupby(spb["소재지"]).count()[["업체명"]]

spb_sort = spb2.sort_values(by=['업체명'], ascending=False)
spb_sort = spb.groupby('소재지').count().reset_index()
spb_sort = spb_sort.sort_values(by=['업체명'], ascending=False)
spb_sort

# 애견 미용 차트
bar_chart2 = alt.Chart(spb_sort).mark_bar(
).encode(
    x=alt.X('소재지',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
    y=alt.Y('업체명',axis=alt.Axis(title=''), sort='-y'),
    color=alt.Color('소재지', scale=alt.Scale(scheme='pinkyellowgreen'), legend=None)
).properties(
)


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
spc_gu = spc_gu.sort_values('data', inplace=True, ascending=False)
spc_gu
# bar_chart3 = alt.Chart(spc_gu).mark_bar(
# ).encode(
#     x=alt.X('gu',axis=alt.Axis(title='',labelFontSize=2.0,labelAngle=-45.0)),
#     y=alt.Y('data',axis=alt.Axis(title=''),sort='-y'),
#     color=alt.Color('gu', scale=alt.Scale(scheme='darkgold'), legend=None)
# ).properties(
# )




col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

with col1 :
  # column 1 에 담을 내용
  st.markdown("**:blue[동물 병원] 이용 순위**")
  st.altair_chart(bar_chart, use_container_width=True)
  st.info('자치구별 동물 병원수 입니다.', icon="ℹ️")
  
  
  st.markdown("**:blue[동물 미용업체] 이용 순위**")
  st.altair_chart(bar_chart2, use_container_width=True)
  st.info('자치구별 동물 미용업체수 입니다.', icon="ℹ️")

  # lightgreyteal
  st.markdown("**:blue[반려동물 보유 비율]**")
  st.altair_chart(bar_chart3, use_container_width=True)
  st.info('자치구별 반려동물 보유비율입니다.', icon="ℹ️")



  # # Text Area
  # message = st.text_area("소개해 드린 추천 채널의 느낀점을 입력해 주세요", "이곳에 입력하세요.")
  # if st.button("Submit", key='message'):
  #   result = message.title()
  #   st.success(result)


with col2 :
  # column 2 에 담을 내용
  st.markdown("**:blue[동물 위탁시설] 이용 순위**")
  st.image("https://user-images.githubusercontent.com/71927533/225590486-ad657a99-8baa-43cd-a474-b23882c96354.png")
  st.info('자치구별 동물 위탁시설 수 입니다.', icon="ℹ️")
  
  
  st.markdown("**:blue[공원 시설] 이용 순위**")
  st.image("https://user-images.githubusercontent.com/71927533/225590467-a09340bf-ad2d-4674-8453-0b4447ff3d93.png")
  st.info('자치구별 공원 시설 수 입니다.', icon="ℹ️")

  st.markdown("**:blue[자치구별 종합] 순위**")
  st.image("https://user-images.githubusercontent.com/71927533/225604387-ac259b04-2a73-48ee-8b3d-296f9cb8f65e.png")
  st.info('자치구별 종합 순위 입니다.', icon="ℹ️")
  
# 데이터 출처 :





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


# fig = px.bar(parksg_gu, x=parksg_gu.index, y='공원 수', color='공원 수',
#              color_continuous_scale='Greens',
#              labels={'x': '자치구', 'y': '공원 수'},
#              height=600)
# fig.update_layout(
#     title='서울시 자치구별 공원 수',
#     xaxis_title='',
#     yaxis_title='공원 수',
#     font=dict(size=18)
# )
# fig.show()

"""# 반려동물 유무 비율"""

# CSV 파일 읽어오기
pet_have = pd.read_csv('data/반려동물+유무+및+취득+경로_20230314161547.csv')

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


# fig = px.bar(pet_have_df, x='gu', y='data', color='data',
#              color_continuous_scale='purp',
#              labels={'gu': '자치구', 'data': '주민 반려동물 보유 비율'},
#              height=600)
# fig.update_layout(
#     title='서울시 자치구별 주민 반려동물 보유 비율',
#     xaxis_title='',
#     yaxis_title='주민 반려동물 보유 비율(%)',
#     font=dict(size=18)
# )
# fig.show()


"""# 종합 순위"""

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
result1_df

# fig = px.bar(result1_df, x='C', y='합계', color='합계',
#              color_continuous_scale='greys',
#              labels={'C': '자치구', '합계': '종합순위'},
#              height=600)
# fig.update_layout(
#     title='서울시 자치구별 반려동물 편의지수 종합순위',
#     xaxis_title='',
#     yaxis_title='편의지수 종합순위',
#     font=dict(size=18)
# )
# fig.show()

"""## 방사형 차트"""

result2 = result[['동물병원순위', '동물미용업체순위', '위탁 업체 수',"보유 비율 순위","공원순위"]]
result2

# 데이터 프레임 생성
# df = pd.DataFrame(result2, index=address)
# # 오각형 방사형 차트 생성 및 출력
# for i in range(len(address)):
#     gn = df.loc[address[i]]
#     # 오각형 방사형 차트 생성
#     fig = px.line_polar(
#         r=gn.values,
#         theta=gn.index,
#         line_close=True,
#     )
#     fig.update_traces(fill='toself')
#     # 차트 레이아웃 설정
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 30]),
#             angularaxis=dict(direction="clockwise"),
#         ),
#         showlegend=False,
#         title=f"{address[i]} 종합 시각화 차트"
#     )
#     # 차트 출력
#     fig.show()
