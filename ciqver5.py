import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

# 한글 폰트 설정 (NanumGothic.ttf가 동일 레퍼지토리에 있다고 가정)
font_path = './NanumGothic.ttf'  # 폰트 파일 경로
fontprop = font_manager.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())  # matplotlib 폰트 설정
rc('font', family=fontprop.get_name())  # seaborn 그래프에서도 한글 설정

# CSV 파일 로드
file_path = 'dashboard.csv'  # 자신의 파일 경로로 변경 필요
data = pd.read_csv(file_path)

# 데이터 전처리: '구분2'와 '구분3'의 결측값을 '제안'으로 대체
data['구분2'].fillna('제안', inplace=True)
data['구분3'].fillna('제안', inplace=True)

# Streamlit 대시보드 시작
st.title("CIQ 데이터 대시보드")

# 1층: 1번과 5번 그래프를 나란히 배치
col1, col2 = st.columns(2)

# 1번 그래프: '발생월'에 따른 원형 그래프
with col1:
    st.subheader("1. 월별 현황 비율 (발생월)")
    fig1, ax1 = plt.subplots()
    data['발생월'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax1)
    ax1.set_ylabel('')
    st.pyplot(fig1)

# 5번 그래프: '보고 구분'에 따른 원형 그래프
with col2:
    st.subheader("5. 보고 구분 비율")
    fig5, ax5 = plt.subplots()
    data['보고 구분'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax5)
    ax5.set_ylabel('')
    st.pyplot(fig5)

# 2번 그래프: '발생월'과 '보고 구분'에 따른 이슈 발생 빈도 그래프
st.subheader("2. 월별 이슈 발생 빈도 (발생월 & 보고 구분)")
fig2, ax2 = plt.subplots(figsize=(12, 6))  # 그래프 크기를 확대
sns.countplot(data=data, x='발생월', hue='보고 구분', ax=ax2)
ax2.set_title('월별 이슈 발생 빈도', fontproperties=fontprop)
ax2.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
st.pyplot(fig2)

# 3번 그래프: '구분2' 상위 5개 항목에 대한 '구분3' 데이터 건수
st.subheader("3. 구분2 상위 5개 항목의 구분3 데이터 건수")
top_5_gu2 = data['구분2'].value_counts().nlargest(5).index  # 구분2 상위 5개 항목
top_5_data = data[data['구분2'].isin(top_5_gu2)]  # 상위 5개 구분2에 해당하는 행만 추출

# 구분3 상위 항목 필터링
top_5_gu3 = top_5_data['구분3'].value_counts().nlargest(5).index  # 구분3 상위 5개 항목
filtered_data = top_5_data[top_5_data['구분3'].isin(top_5_gu3)]  # 구분3 상위 5개에 해당하는 데이터 필터링

fig3, ax3 = plt.subplots(figsize=(12, 6))  # 그래프 크기 확대
sns.countplot(data=filtered_data, x='구분2', hue='구분3', ax=ax3)
ax3.set_title('구분2 상위 5개 항목의 구분3 데이터 건수', fontproperties=fontprop)
ax3.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
st.pyplot(fig3)

# 4번 그래프: '발생월'과 'E:P'에 따른 제품군 빈도 그래프
st.subheader("4. 월별 제품군 빈도 (발생월 & E:P)")
fig4, ax4 = plt.subplots(figsize=(12, 6))  # 그래프 크기를 확대
sns.countplot(data=data, x='발생월', hue='E:P', ax=ax4)
ax4.set_title('월별 제품군 빈도', fontproperties=fontprop)
ax4.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
st.pyplot(fig4)
