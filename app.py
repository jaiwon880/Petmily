# streamlit 라이브러리 호출
import streamlit as st

st.title("팻밀리")

st.subheader("반려견 행복지도")



#@title 라이브러리 및 모듈 불러오기
# 분석 기본 라이브러리

import pandas as pd
import numpy as np

# 시각화
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# %matplotlib inline
# import seaborn as sns

#한글 폰트 처리
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

#한글 폰트를 나눔폰트로 설정
# plt.rc('font', family='NanumBarunGothic')

url = "https://github.com/whataLIN/sample_rp/raw/main"
# 서울시 동물병원 파일 불러오기
seoul_pet_hospital = pd.read_csv(url + '/data/PetHospital.csv', encoding = 'cp949')
# 서울시 애견미용업장 파일 불러오기
# seoul_pet_beauty = pd.read_excel(url + '/data/PetBeautyShop.xls') 
# 서울시 애견위탁관리 파일 불러오기
seoul_pet_consignment = pd.read_csv(url + '/data/PetHotel.csv')
# seoul_pet_consignment = pd.read_csv(url + '/data/PetHotel.csv', encoding = 'cp949')
# 서울시 주요 공원 현황 파일 불러오기
seoul_park = pd.read_csv(url + '/data/SeoulPark.csv', encoding = 'cp949')
# 반려동물 유무 비율 보유 파일 불러오기ㅖ
seoul_pet_own = pd.read_csv(url + '/data/HowManyPeoPle.csv')


def drawGraph(X, Y, title, colormap):

    # 그라데이션 색상을 위한 컬러 맵 생성
    cmap = plt.get_cmap(colormap)

    # 데이터프레임에서 값을 가져와서 바차트를 그립니다.
    fig, ax = plt.subplots(figsize = (20, 10))

    bars = ax.bar(x, y, align='center')

    # 그라데이션 색상 적용
    for i, bar in enumerate(bars):
        bar.set_color(cmap(i / len(X)))

    # x축 레이블 설정
    plt.xticks(rotation = 45, fontsize = 15)

    # 그래프 타이틀 설정
    plt.title('title')

    # 그래프 출력
    plt.show()




#동물병원 그래프
def seoulPetHospital():

    import re

    sph = seoul_pet_hospital.copy()
    sph = sph.dropna(how='all')

    cols1 = ["총직원수", "인허가일자", "인허가취소일자","상세영업상태코드","최종수정시점","데이터갱신구분","업태구분명","데이터갱신일자", "상세업무구분명", "개방자치단체코드","관리번호","영업상태구분코드","폐업일자",
         "휴업시작일자","소재지면적","소재지우편번호", "상세영업상태명","휴업종료일자", "재개업일자","개방서비스아이디","권리주체일련번호","업무구분명"]

    for col in cols1:
        del sph[col]

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
                "강서구",
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

    st.bar_chart(sph_sort, x=ph_sort.index, y=sph_sort['사업장명'], width=20, height=10, use_container_width=True)
    # #==============
    # #그래프그리기
    # # 그라데이션 색상을 위한 컬러 맵 생성
    # cmap = plt.get_cmap('winter')

    # # 데이터프레임에서 값을 가져와서 바차트를 그립니다.
    # fig, ax = plt.subplots(figsize = (20, 10))
    # bars = ax.bar(sph_sort.index, sph_sort['사업장명'], align='center')

    # # 그라데이션 색상 적용
    # for i, bar in enumerate(bars):
    #     bar.set_color(cmap(i / len(sph_sort.index)))

    # # x축 레이블 설정
    # plt.xticks(rotation = 45, fontsize = 15)

    # # 그래프 타이틀 설정
    # plt.title('서울시 자치구별 동물병원 수')

    # # 그래프 출력
    # plt.show()





#애견미용업장
def seoulBetBeauty():

    spb = seoul_pet_beauty.copy()
    cols1 = ["번호", "인허가 정보", "이전인허가정보"]

    for col in cols1:
        del spb[col]

    import re

    pattern = '|'.join(sph_list)
    spb['소재지'] = spb['소재지'].str.extract(f'({pattern})', flags=re.IGNORECASE)

    spb2 = spb.groupby(spb["소재지"]).count()[["업체명"]]
    spb_sort = spb2.sort_values(by=['업체명'], ascending=False)

    # 그라데이션 색상을 위한 컬러 맵 생성
    cmap = plt.get_cmap('spring')

    # 데이터프레임에서 값을 가져와서 바차트를 그립니다.
    fig, ax = plt.subplots(figsize = (20, 10))
    bars = ax.bar(spb_sort.index, spb_sort['업체명'], align='center')

    # 그라데이션 색상 적용
    for i, bar in enumerate(bars):
        bar.set_color(cmap(i / len(spb_sort.index)))

    # x축 레이블 설정
    plt.xticks(rotation = 45, fontsize = 15)

    # 그래프 타이틀 설정
    plt.title('서울시 자치구별 동물미용업체 수')

    # 그래프 출력
    plt.show()




#위탁관리업장
def seoulPetCon():
    seoul_pet_con = pd.read_csv("data/동물위탁관리업.csv")
    spc = seoul_pet_con.groupby([seoul_pet_con["개방서비스명"],seoul_pet_con["소재지전체주소"]])
    spc2 = spc[["소재지전체주소"]].count().rename(columns={"소재지전체주소": "개수"})
    dict1 = spc2.iloc[1:].loc[:,'개수'].reset_index(level=0, drop=True).to_dict()

    import copy
    dict2 = copy.deepcopy(dict1)
    dict2_keys_list = list(dict2.keys())
    dict2_values_list = list(dict2.values())
    dict2_keys_list2 = [x + "구" for x in dict2_keys_list]
    dict2_keys_list3 = [x.replace("서울특별시", "") for x in dict2_keys_list2]
    done_dict = dict(zip(dict2_keys_list3, dict2_values_list))
    sorted_items = sorted(done_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_done_dict = dict(sorted_items)

    spc_gu = pd.DataFrame(sorted_done_dict.items(), columns=['gu', 'data'])
    spc_gu['data'] = spc_gu['data'].astype('float')
    spc_gu.sort_values('data', inplace=True, ascending=False)

    # 그라데이션 색상을 위한 컬러 맵 생성
    cmap = plt.get_cmap('coolwarm')
    # 데이터프레임에서 값을 가져와서 바차트를 그립니다.
    fig, ax = plt.subplots(figsize = (20, 10))
    # bars = ax.bar(list(sorted_dict2.keys())[::-1], list(sorted_dict2.values())[::-1], align='center')
    bars = ax.bar(spc_gu.gu, spc_gu.data, align='center')
    # 그라데이션 색상 적용
    for i, bar in enumerate(bars):
        bar.set_color(cmap(i / len(list(sorted_dict2.keys()))))
    # x축 레이블 설정
    plt.xticks(rotation = 45, fontsize = 15)
    # 그래프 타이틀 설정
    plt.title('서울시 자치구별 주민 반려동물 보유 비율')
    # 그래프 출력
    plt.show()





#공원
def seoulPark():
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

    # 그라데이션 색상을 위한 컬러 맵 생성
    cmap = plt.get_cmap('summer')

    fig, ax = plt.subplots(figsize = (20, 10))
    bars_park = ax.bar(parksg_gu.index, parksg_gu['공원 수'], align='center')

    plt.title("서울시 자치구별 공원 수")
    plt.xlabel("자치구")
    plt.ylabel("공원 수")
    plt.xticks(rotation = 45, fontsize = 15)

    # 그라데이션 색상 적용
    for i, bar in enumerate(bars_park):
        bar.set_color(cmap(i / len(parksg_gu)))

    # 그래프 출력
    plt.show()
        




#유무 비율
def WhoHavePet():
    # CSV 파일 읽어오기
    pet_have = pd.read_csv('data/반려동물+유무+및+취득+경로_20230314161547.csv')

    # 특정열에 특정값을 가진 행 추출하기
    pet_have2 = pet_have[pet_have['구분별(1)'].str.contains("지역소분류")]

    # 추출된 데이터를 새로운 CSV 파일로 저장하기
    pet_have2.to_csv('반려동물 유무.csv', index=False)

    pet_have_dict = dict(zip(pet_have2['구분별(2)'], pet_have2['2021']))

    import copy
    pet_have_dict2 = copy.deepcopy(pet_have_dict)

    pet_have_dict_sorted_items = sorted(pet_have_dict2.items(), key=lambda x: x[1], reverse=True)
    pet_have_dict_sorted = dict(pet_have_dict_sorted_items)

    pet_have_df = pd.DataFrame(pet_have_dict_sorted.items(), columns=['gu', 'data'])
    pet_have_df['data'] = pet_have_df['data'].astype('float')
    pet_have_df.sort_values('data', inplace=True, ascending=False)

    import matplotlib.pyplot as plt

    # 그라데이션 색상을 위한 컬러 맵 생성
    cmap = plt.get_cmap('coolwarm')
    # 데이터프레임에서 값을 가져와서 바차트를 그립니다.
    fig, ax = plt.subplots(figsize = (20, 10))
    # bars = ax.bar(list(sorted_dict2.keys())[::-1], list(sorted_dict2.values())[::-1], align='center')
    bars = ax.bar(pet_have_df.gu, pet_have_df.data, align='center')
    # 그라데이션 색상 적용
    for i, bar in enumerate(bars):
        bar.set_color(cmap(i / len(list(pet_have_dict_sorted.keys()))))
    # x축 레이블 설정
    plt.xticks(rotation = 45, fontsize = 15)
    # 그래프 타이틀 설정
    plt.title('서울시 자치구별 주민 반려동물 보유 비율')
    # 그래프 출력
    plt.show()



#==========================================================

# st.sidebar.title('시간 순삭 유튜브 추천👇')
# add_selectbox = st.sidebar.selectbox("주인장 추천 채널",
#  ["지식한입", "ITSub잇섭", "느낌적인느낌","호갱구조대", "너 진짜 똑독하다", "슈카월드"])

# values = st.sidebar.slider('추천 채널 만족도를 평가', 1, 5)
# st.sidebar.write('평가 점수:', values)


# col1,col2 = st.columns([1,1])
# # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

# with col1 :
#   # column 1 에 담을 내용
#   st.markdown("**나에게 :blue[가장 도움이 될 것 같은] 유튜브**")

#   st.image("https://user-images.githubusercontent.com/71927533/221650828-c1a86b95-99ac-4a85-a4cc-e398eaf2865f.jpg")
#   st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon="ℹ️")
  
#   # Text Area
#   message = st.text_area("소개해 드린 추천 채널의 느낀점을 입력해 주세요", "이곳에 입력하세요.")
#   if st.button("Submit", key='message'):
#     result = message.title()
#     st.success(result)

#   st.write(
#     """
#     > 출처: [빵형의 개발도상국](https://www.youtube.com/@bbanghyong/), [노마드 코더](https://www.youtube.com/@nomadcoders)
    
#     """)


# with col2 :
#   # column 2 에 담을 내용
#   st.markdown("**:red[남]이보면 좋을 것 같은 유튜브**")
#   st.image("https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg")
#   st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon="ℹ️")
  



seoulPetHospital()