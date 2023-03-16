# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법

# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법

import pandas as pd
import requests
from datetime import datetime
import pytz
from streamlit.components.v1 import html


def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%8F%99%EB%AC%BC%EC%9C%84%ED%83%81%EA%B4%80%EB%A6%AC%EC%97%85.csv"
  # df을 읽어 오면서 df언네임 삭제
  seoul_pet_consignment = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  seoul_pet_consignment.index += 1
  # df 반환
  return seoul_pet_consignment

def create_df1():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC%2B%EC%9C%A0%EB%AC%B4%2B%EB%B0%8F%2B%EC%B7%A8%EB%93%9D%2B%EA%B2%BD%EB%A1%9C_20230314161547.csv"
  # df을 읽어 오면서 df언네임 삭제
  seoul_pet_own = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  seoul_pet_own.index += 1
  # df 반환
  return seoul_pet_own

def create_df2():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC%2B%EC%9C%A0%EB%AC%B4%2B%EB%B0%8F%2B%EC%B7%A8%EB%93%9D%2B%EA%B2%BD%EB%A1%9C_20230314161547.csv"
  # df을 읽어 오면서 df언네임 삭제
  seoul_park = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  seoul_park.index += 1
  # df 반환
  return seoul_park

def create_df3():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv"
  # df을 읽어 오면서 df언네임 삭제
  seoul_pet_hospital = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  seoul_pet_hospital.index += 1
  # df 반환
  return seoul_pet_hospital

def create_df4():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv"
  # df을 읽어 오면서 df언네임 삭제
  seoul_pet_beauty = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  seoul_pet_beauty.index += 1
  # df 반환
  return seoul_pet_beauty

seoul_pet_hospital = pd.read_csv('https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv')
sph = seoul_pet_hospital.copy()
sph = Preprocess(sph)
sph = sph.dropna(how='all')

sph



# import re

# sph = seoul_pet_hospital.copy()
# sph = sph.dropna(how='all')

# #@title 필요없는 컬럼들 제거
# cols1 = ["총직원수", "인허가일자", "인허가취소일자","상세영업상태코드","최종수정시점","데이터갱신구분","업태구분명","데이터갱신일자", "상세업무구분명", "개방자치단체코드","관리번호","영업상태구분코드","폐업일자",
#          "휴업시작일자","소재지면적","소재지우편번호", "상세영업상태명","휴업종료일자", "재개업일자","개방서비스아이디","권리주체일련번호","업무구분명"]

# for col in cols1:
#     del sph[col]

# sph = sph[sph['소재지전체주소'].str.contains('서울', na=False)]

# sph_list = ["강서구",
#             "양천구",
#             "구로구",
#             "금천구",
#             "영등포구",
#             "동작구",
#             "관악구",
#             "서초구",
#             "강남구",
#             "송파구",
#             "강동구",
#             "마포구",
#             "은평구",
#             "서대문구",
#             "종로구",
#             "중구",
#             "용산구",
#             "성북구",
#             "성동구",
#             "동대문구",
#             "광진구",
#             "중랑구",
#             "노원구",
#             "도봉구",
#             "강북구"
# ]

# pattern = '|'.join(sph_list)
# sph['소재지전체주소'] = sph['소재지전체주소'].str.extract(f'({pattern})', flags=re.IGNORECASE)


# sph_gu=(sph.groupby(sph['소재지전체주소']).count())[["사업장명"]]
# sph_gu

# sph_sort = sph_gu.sort_values(by=['사업장명'], ascending=False)
# sph_sort


# import plotly.express as px
# fig = px.bar(sph_sort, x=sph_sort.index, y='사업장명', color='사업장명',
#              color_continuous_scale='Blues',
#              labels={'x': '자치구', 'y': '동물병원 수'},
#              height=600)
# fig.update_layout(
#     title='서울시 자치구별 동물병원 수',
#     xaxis_title='',
#     yaxis_title='동물병원 수',
#     font=dict(size=18)
# )
# fig.show()


# def create_df():
#   # DF_URL
#   df_URL = ["https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%8F%99%EB%AC%BC%EC%9C%84%ED%83%81%EA%B4%80%EB%A6%AC%EC%97%85.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC%2B%EC%9C%A0%EB%AC%B4%2B%EB%B0%8F%2B%EC%B7%A8%EB%93%9D%2B%EA%B2%BD%EB%A1%9C_20230314161547.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%A3%BC%EC%9A%94%20%EA%B3%B5%EC%9B%90%ED%98%84%ED%99%A9.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%95%A0%EA%B2%AC%EB%AF%B8%EC%9A%A9%EC%97%85%EC%9E%A5.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv"]

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

st.sidebar.title('서울시 자치구를 선택해주세요👇')
choice = st.sidebar.selectbox("자치구 선택",
["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구","중랑구"]
)
st.image(gu_dict[choice], use_column_width=True)


# tmp_df = df[df['species']== add_selectbox]
# st.table(tmp_df.head())


col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

with col1 :
  # column 1 에 담을 내용
  st.markdown("**:blue[동물 병원] 이용 순위**")
  st.image("https://user-images.githubusercontent.com/71927533/225588437-0a7d6c29-27fa-48d9-b652-54573a4e35b6.png")
  st.info('자치구별 동물 병원수 입니다.', icon="ℹ️")
  
  
  st.markdown("**:blue[동물 미용업체] 이용 순위**")
  st.image("https://user-images.githubusercontent.com/71927533/225588981-d31e33b5-12c5-4d9f-bbfb-6da3b511a800.png")
  st.info('자치구별 동물 미용업체수 입니다.', icon="ℹ️")


  st.markdown("**:blue[반려동물 보유 비율]**")
  st.image("https://user-images.githubusercontent.com/71927533/225590064-1171e04b-455a-4308-92d5-9cf8495c1291.png")
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
  
