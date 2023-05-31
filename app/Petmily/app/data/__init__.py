import streamlit as st
import pandas as pd
import re
import copy

def read_csv(filename, cp949=False):
    return pd.read_csv(
        f"static/{filename}",
        encoding=('utf-8' if not cp949 else 'cp949'))

@st.cache_data
def get_seoul_pet_hospital() -> pd.DataFrame:
    '''서울시 동물병원 파일 불러오기'''
    return read_csv("hospital.csv", cp949=True).dropna(how='all')[["번호", "개방서비스명", "영업상태명", '소재지전화', '소재지전체주소', '도로명전체주소', '도로명우편번호',
    '사업장명', '좌표정보(x)', '좌표정보(y)']]

@st.cache_data
def get_sph_sort():
    sph = get_seoul_pet_hospital()
    pattern = get_seoul_gu(pattern=True)
    sph['소재지전체주소'] = sph['소재지전체주소'].str.extract(f'({pattern})', flags=re.IGNORECASE)
    sph_gu=(sph.groupby(sph['소재지전체주소']).count())[["사업장명"]]
    return sph_gu.sort_values(by=['사업장명'], ascending=False)

@st.cache_data
def get_seoul_gu(pattern=False) -> pd.DataFrame:
    df = get_seoul_pet_hospital()
    df_seoul_gu = df[
        df['소재지전체주소'].str.contains('서울', na=False)
    ]['소재지전체주소'].str.split(expand=True)[1].unique()
    sph_list = sorted([gu for gu in df_seoul_gu if '구' in gu])
    return sph_list if not pattern else '|'.join(sph_list)

@st.cache_data
def get_seoul_pet_beauty() -> pd.DataFrame:
    '''서울시 애견미용업장 파일 불러오기'''
    return read_csv("beauty.csv")

@st.cache_data
def get_spb_sort() -> pd.DataFrame:
    spb = get_seoul_pet_beauty()
    spb.drop(['번호', '인허가 정보', '이전인허가정보'], axis=1, inplace=True)
    pattern = get_seoul_gu(pattern=True)
    spb['소재지'] = spb['소재지'].str.extract(f'({pattern})', flags=re.IGNORECASE)
    spb2 = spb.groupby(spb["소재지"]).count()[["업체명"]]
    return spb2.sort_values(by=['업체명'], ascending=False)

@st.cache_data
def get_seoul_pet_hotel() -> pd.DataFrame:
    '''서울시 동물위탁관리업 파일 불러오기'''
    return read_csv("hotel.csv")

@st.cache_data
def get_seoul_park() -> pd.DataFrame:
    '''서울시 주요 공원 현황 파일 불러오기'''
    return read_csv('park.csv', cp949=True)

@st.cache_data
def get_park_gu():
    seoul_park = get_seoul_park()

    park_info= seoul_park[["연번","공원명","공원주소"]].copy()

    def change_addr(index, new_addr):
        park_info.loc[index, '공원주소'] = new_addr

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

    return parksg_gu

@st.cache_data
def get_pet_rate() -> pd.DataFrame:
    '''반려동물 유무 비율 보유 파일 불러오기'''
    return read_csv('own.csv')

@st.cache_data
def get_pet_have():
    # 반려동물 CSV 파일 읽어오기
    pet_have = get_pet_rate()
    # 특정열에 특정값을 가진 행 추출하기
    pet_have2 = pet_have[pet_have['구분별(1)'].str.contains("지역소분류")]
    pet_have_dict = dict(zip(pet_have2['구분별(2)'], pet_have2['2021']))
    pet_have_dict2 = copy.deepcopy(pet_have_dict)
    pet_have_dict_sorted_items = sorted(pet_have_dict2.items(), key=lambda x: x[1], reverse=True)
    pet_have_dict_sorted = dict(pet_have_dict_sorted_items)
    pet_have_df = pd.DataFrame(pet_have_dict_sorted.items(), columns=['gu', 'data'])
    pet_have_df['data'] = pet_have_df['data'].astype('float')
    pet_have_df.sort_values('data', inplace=True, ascending=False)
    return pet_have_df

@st.cache_data
def get_spc_gu():
    seoul_pet_con = get_seoul_pet_hotel()
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
    return spc_gu

@st.cache_data
def get_result():
    sph_sort = get_sph_sort()
    sph_sort["동물병원순위"] = sph_sort['사업장명'].rank(method='min', ascending=True)

    spb_sort = get_spb_sort()
    spb_sort["동물미용업체순위"] = spb_sort['업체명'].rank(method='min', ascending=True)
    
    parks_rank = get_park_gu()
    parks_rank['공원순위'] = parks_rank['공원 수'].rank(method='min', ascending=True)

    pet_have_df = get_pet_have()
    pet_have_df['보유 비율 순위'] = pet_have_df['data'].rank(method='min', ascending=True)
    pet_have_df_rank = pet_have_df[['gu', '보유 비율 순위']]
    pet_have_df_rank = pet_have_df_rank.set_index("gu")

    spc_gu = get_spc_gu()
    spc_gu['위탁 업체 수'] = spc_gu['data'].rank(method='min', ascending=True)
    pet_cs = spc_gu[['gu', '위탁 업체 수']]
    pet_cs2=pet_cs.set_index("gu")

    address = get_seoul_gu()
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
    return result