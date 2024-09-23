import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. 폰트 파일 경로 설정
font_path = os.path.join(os.getcwd(), 'NanumGothic.ttf')
if not os.path.exists(font_path):
    st.error(f"폰트 파일을 찾을 수 없습니다. 현재 경로에 'NanumGothic.ttf' 파일이 있는지 확인하세요.")
else:
    # CSV 파일 로드
    file_path = 'dashboard.csv'  # 자신의 파일 경로로 변경 필요
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
    except FileNotFoundError:
        st.error(f"CSV 파일을 찾을 수 없습니다. '{file_path}' 파일 경로를 확인하세요.")
    else:
        # 데이터 전처리: '구분2'와 '구분3'의 결측값을 '제안'으로 대체
        data['구분2'].fillna('제안', inplace=True)
        data['구분3'].fillna('제안', inplace=True)
        data['E:P'] = data['E:P'].str[4:]
        data = data[data['E:P'] != '타']
        data = data[data['보고 구분'] != '열교환기']
        # Streamlit 대시보드 시작
        st.title("CIQ 데이터 대시보드")

        # 색상 팔레트 설정
        color_palette = px.colors.qualitative.Plotly

         # 1번 그래프: '발생월'에 따른 원형 그래프
        st.subheader("월별 품질정보 등록 비율")
        # '발생월'을 1월부터 12월까지 순서대로 정렬
        data['발생월'] = pd.Categorical(data['발생월'], categories=[f"{i}월" for i in range(1, 13)], ordered=True)
        fig1 = px.pie(data, names='발생월', title='월별 품질정보 등록 비율', color_discrete_sequence=color_palette,
                      category_orders={'발생월': [f"{i}월" for i in range(1, 13)]})
        fig1.update_layout(font=dict(family="NanumGothic", size=18))
        st.plotly_chart(fig1)

        # 2번 그래프: '보고 구분'에 따른 원형 그래프
        st.subheader("불량 유형 비율")
        fig5 = px.pie(data, names='보고 구분', title='불량 유형 비율')
        fig5.update_layout(font=dict(family="NanumGothic", size=18))
        st.plotly_chart(fig5)
        
        # 3번 그래프: '발생월'과 '보고 구분'에 따른 이슈 발생 빈도 그래프
        st.subheader("월별 불량 유형별 발생 빈도")
        fig2 = px.histogram(data, x='발생월', color='보고 구분', barmode='group', title='월별 불량 유형별 발생 빈도')
        fig2.update_layout(font=dict(family="NanumGothic", size=18))
        st.plotly_chart(fig2)

        # 4번 그래프: '구분2' 상위 5개 항목과 구분3 상위 3개 데이터
        st.subheader("불량 부품 TOP 5 상세 불량 현황")
        top_5_gu2 = data['구분2'].value_counts().nlargest(5).index  # 구분2 상위 5개 항목

        filtered_data = pd.DataFrame()
        for gu2 in top_5_gu2:
            gu3_counts = data[data['구분2'] == gu2]['구분3'].value_counts().nlargest(3)
            gu3_data = pd.DataFrame({'불량 부품': gu2, '구분3': gu3_counts.index, 'count': gu3_counts.values})
            filtered_data = pd.concat([filtered_data, gu3_data], axis=0)

        fig3 = px.bar(filtered_data, x='불량 부품', y='count', color='구분3', title='불량 부품 TOP 5 상세 불량 현황', barmode='group')
        fig3.update_layout(font=dict(family="NanumGothic", size=18))
        st.plotly_chart(fig3)

        # 5번 그래프: '발생월'과 'E:P'에 따른 제품군 빈도 그래프
        st.subheader("월별 제품군 빈도")
        fig4 = px.histogram(data, x='발생월', color='E:P', barmode='group', title='월별 제품군 빈도')
        fig4.update_layout(font=dict(family="NanumGothic", size=18))
        st.plotly_chart(fig4)
