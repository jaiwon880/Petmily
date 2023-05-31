import streamlit as st 
import plotly.express as px
import pandas as pd
import copy
import data

def sidebar():
    with st.sidebar:
        st.title('자치구를 선택해주세요! 👇')
        st.selectbox(
            "자치구 선택",
            data.get_seoul_gu(),
            key='select_gu'
        )

def hospital_chart():
    sph_sort = data.get_sph_sort()
    fig = px.bar(sph_sort, x=sph_sort.index,
                y='사업장명', color='사업장명',
                color_continuous_scale='Blues',
                labels={'x': '자치구', 'y': '동물병원 수'},
                height=400)
    fig.update_layout(
        title='서울시 자치구별 동물병원 수',
        showlegend=False,
        xaxis_title='',
        yaxis_title='동물병원 수',
        font=dict(size=3),
    )
    fig.update_xaxes(tickfont_size=7,tickangle=45)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.info('자치구별 동물 병원수 입니다.', icon="ℹ️")

def beauty_chart():
    spb_sort = data.get_spb_sort()
    fig_beauty = px.bar(
        spb_sort, x=spb_sort.index, y='업체명', color='업체명',
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
    st.plotly_chart(fig_beauty, theme="streamlit", use_container_width=True)
    st.info('자치구별 동물 미용업체수 입니다.', icon="ℹ️")

def tf_chart():
    pet_have_df = data.get_pet_have()
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
    st.plotly_chart(fig_tf, theme="streamlit", use_container_width=True)
    st.info('자치구별 반려동물 보유비율입니다.', icon="ℹ️")

def hotel_chart():
    # 서울시 애견위탁관리 파일 불러오기
    # 번호, 구분(위탁관리 포함된 문자만), 업체명, 소재지
    spc_gu = data.get_spc_gu()

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
    st.plotly_chart(fig_con, theme="streamlit",
    use_container_width=True)
    st.info('자치구별 동물 위탁시설 수 입니다.', icon="ℹ️")

def park_chart():
    # 서울시 주요 공원 현황 파일 불러오기
    # 연번, 공원명, 공원개요("맑은 공기"), 면적, 주요 시설, 주요 식물, 공원주소, 관리부서, 전화번호, 바로가기

    parksg_gu = data.get_park_gu()

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
    st.plotly_chart(fig_park, theme="streamlit", use_container_width=True)
    st.info('자치구별 공원 시설 수 입니다.', icon="ℹ️")

def syn_chart():
    result = data.get_result()
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
    st.plotly_chart(fig_syn, theme="streamlit", use_container_width=True)
    st.info('자치구별 종합 순위 입니다.', icon="ℹ️")

def radar_chart():
    address = data.get_seoul_gu()
    result2 = data.get_result()[['동물병원순위', '동물미용업체순위', '위탁 업체 수',"보유 비율 순위","공원순위"]]
    # 오각형 방사형 차트 생성 및 출력
    # 데이터 프레임 생성
    df = pd.DataFrame(result2, index=address)
    # 사이드바에서 자치구 선택
    # 선택한 자치구에 해당하는 데이터 추출
    selected_region = st.session_state['select_gu']
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