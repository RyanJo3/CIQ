import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 시스템 폰트 설정 (Windows에서는 'Malgun Gothic', macOS에서는 'AppleGothic', Linux에서는 'Noto Sans CJK' 권장)
plt.rcParams['font.family'] = '굴림 보통'  # 또는 'AppleGothic', 'Noto Sans CJK' 등
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# seaborn에서 한글 폰트 적용
sns.set(font='굴림 보통')  # 시스템 폰트로 변경

# CSV 파일 로드
file_path = 'dashboard.csv'  # 자신의 파일 경로로 변경 필요
data = pd.read_csv(file_path)

# 데이터 전처리: '구분2'와 '구분3'의 결측값을 '제안'으로 대체
data['구분2'].fillna('제안', inplace=True)
data['구분3'].fillna('제안', inplace=True)

# Streamlit 대시보드 시작
st.title("CSV 데이터 대시보드")

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
fig2, ax2 = plt.subplots(figsize=(19, 9))  # 그래프 크기를 확대
sns.countplot(data=data, x='발생월', hue='보고 구분', ax=ax2)
ax2.set_title('월별 이슈 발생 빈도')  # fontproperties 제거
ax2.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
st.pyplot(fig2)

# 3번 그래프: '구분2' 상위 5개 항목과 구분3 상위 3개 데이터
st.subheader("3. 구분2 상위 5개 항목의 구분3 상위 3개 데이터 건수")
top_5_gu2 = data['구분2'].value_counts().nlargest(5).index  # 구분2 상위 5개 항목

filtered_data = pd.DataFrame()
for gu2 in top_5_gu2:
    gu3_counts = data[data['구분2'] == gu2]['구분3'].value_counts().nlargest(3)
    gu3_data = pd.DataFrame({'구분2': gu2, '구분3': gu3_counts.index, '건수': gu3_counts.values})
    filtered_data = pd.concat([filtered_data, gu3_data], axis=0)

fig3, ax3 = plt.subplots(figsize=(19, 9))  # 그래프 크기 확대
sns.barplot(data=filtered_data, x='구분2', y='건수', hue='구분3', ax=ax3)
ax3.set_title('구분2 상위 5개 항목의 구분3 상위 3개 데이터 건수')  # fontproperties 제거
ax3.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 범례를 그래프 바깥으로 이동
st.pyplot(fig3)

# 4번 그래프: '발생월'과 'E:P'에 따른 제품군 빈도 그래프
st.subheader("4. 월별 제품군 빈도 (발생월 & E:P)")
fig4, ax4 = plt.subplots(figsize=(19, 9))  # 그래프 크기를 확대
sns.countplot(data=data, x='발생월', hue='E:P', ax=ax4)
ax4.set_title('월별 제품군 빈도')  # fontproperties 제거
ax4.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)  # 범례를 그래프 바깥으로 이동하고 가로로 배치
st.pyplot(fig4)
