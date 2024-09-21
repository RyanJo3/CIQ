import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import os

# 1. 폰트 파일 경로 설정
font_path = os.path.join(os.getcwd(), 'NanumGothic.ttf')
if not os.path.exists(font_path):
    st.error(f"폰트 파일을 찾을 수 없습니다. 현재 경로에 'NanumGothic.ttf' 파일이 있는지 확인하세요.")
else:
    # 2. 폰트 추가
    fm.fontManager.addfont(font_path)
    font_prop = fm.FontProperties(fname=font_path)  # 폰트 속성 정의
    plt.rc('font', family='NanumGothic')  # matplotlib에 폰트 설정
    sns.set(font='NanumGothic')  # seaborn에 폰트 설정

    # 3. 설정된 폰트 확인
    st.write(f"설정된 폰트: {font_prop.get_name()}")

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

        # Streamlit 대시보드 시작
        st.title("CIQ 데이터 대시보드")

        # 1층: 1번과 5번 그래프를 나란히 배치
        col1, col2 = st.columns(2)

        # 1번 그래프: '발생월'에 따른 원형 그래프
        with col1:
            st.subheader("월별 품질정보 등록 비율")
            fig1, ax1 = plt.subplots()
            data['발생월'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax1)
            ax1.set_ylabel('')
            st.pyplot(fig1)

        # 5번 그래프: '보고 구분'에 따른 원형 그래프
        with col2:
            st.subheader("불량 유형 비율")
            fig5, ax5 = plt.subplots(figsize=(10, 10))  # 그래프 크기 조정 (가로, 세로)
    
            # 데이터 준비
            counts = data['보고 구분'].value_counts()
    
            # explode를 사용하여 각 조각을 띄움
            explode = [0.1] * len(counts)  # 모든 조각을 0.1만큼 띄움

            # 원형 그래프 그리기
            patches, texts, autotexts = ax5.pie(
                counts,
                explode=explode,
                labels=None,  # 레이블 숨김
                autopct='%1.1f%%',
                startangle=90,
                colors=sns.color_palette("husl", len(counts)),  # 색상 설정
                textprops=dict(color="w"),
            )

            # 별도의 범례 추가
            ax5.legend(patches, counts.index, title="보고 구분", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

            ax5.set_ylabel('')

            # 레이블 겹침을 줄이기 위해 축의 비율을 조정
            ax5.axis('equal')  # 원형으로 보이게 조정
            st.pyplot(fig5)

        # 2번 그래프: '발생월'과 '보고 구분'에 따른 이슈 발생 빈도 그래프
        st.subheader("월별 이슈 발생 빈도")
        fig2, ax2 = plt.subplots(figsize=(19, 9))  # 그래프 크기를 확대
        sns.countplot(data=data, x='발생월', hue='보고 구분', ax=ax2)
        ax2.set_title('월별 이슈 발생 빈도')  # fontproperties 제거
        ax2.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
        st.pyplot(fig2)

        # 3번 그래프: '구분2' 상위 5개 항목과 구분3 상위 3개 데이터
        st.subheader("불량 부품 TOP 5 상세 불량 현황")
        top_5_gu2 = data['구분2'].value_counts().nlargest(5).index  # 구분2 상위 5개 항목

        filtered_data = pd.DataFrame()
        for gu2 in top_5_gu2:
            gu3_counts = data[data['구분2'] == gu2]['구분3'].value_counts().nlargest(3)
            gu3_data = pd.DataFrame({'구분2': gu2, '구분3': gu3_counts.index, '건수': gu3_counts.values})
            filtered_data = pd.concat([filtered_data, gu3_data], axis=0)

        fig3, ax3 = plt.subplots(figsize=(19, 9))  # 그래프 크기 확대
        sns.barplot(data=filtered_data, x='구분2', y='건수', hue='구분3', ax=ax3)
        ax3.set_title('불량 부품 TOP 5 상세 불량 현황')  # fontproperties 제거
        ax3.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
        st.pyplot(fig3)

        # 4번 그래프: '발생월'과 'E:P'에 따른 제품군 빈도 그래프
        st.subheader("월별 제품군 빈도")
        fig4, ax4 = plt.subplots(figsize=(19, 9))  # 그래프 크기를 확대
        sns.countplot(data=data, x='발생월', hue='E:P', ax=ax4)
        ax4.set_title('월별 제품군 빈도')  # fontproperties 제거
        ax4.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)  # 범례를 그래프 바깥으로 이동하고 가로로 배치
        st.pyplot(fig4)
