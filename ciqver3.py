import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.font_manager as fm
import os

# 한글 폰트 경로 설정
font_path = 'NanumGothic.ttf'  # 실제 폰트 파일 경로로 수정
if not os.path.exists(font_path):
    st.error(f"폰트 파일이 존재하지 않습니다: {font_path}")

font_prop = fm.FontProperties(fname=font_path)

st.set_page_config(page_title="CIQ Dashboard", layout="wide")

# 추가한 한글 폰트 적용을 위한 스타일 지정
st.markdown(
    """
    <style>
    * {
        font-family: 'NanumGothic', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Matplotlib 폰트 설정
plt.rc('font', family='NanumGothic')

def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"CSV 파일이 존재하지 않습니다: {file_path}")
        return pd.DataFrame()  # 빈 데이터프레임 반환
    df = pd.read_csv(file_path)
    if '구분2' in df.columns:
        df['구분2'] = df['구분2'].fillna('제안')
    return df

def visualize_data(df):
    st.title("CIQ 데이터 시각화 대시보드")

    if df.empty:
        st.warning("데이터가 없습니다.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("발생월 별 불량 유형 분포 (Boxplot)")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='발생월', y='보고 구분', palette='Set3', ax=ax)
        ax.set_title('발생월 별 불량 유형 분포', fontsize=16, fontproperties=font_prop)
        ax.set_xlabel('발생월', fontsize=14, fontproperties=font_prop)
        ax.set_ylabel('보고 구분', fontsize=14, fontproperties=font_prop)
        st.pyplot(fig)
    with col2:
        st.subheader("불량 부품 별 상위 10개 항목 월별 건수 분포 (Lineplot)")
        top_10_parts = df['구분2'].value_counts().nlargest(10).index
        filtered_df = df[df['구분2'].isin(top_10_parts)]
    
        if filtered_df.empty:
            st.warning("상위 10개 부품 데이터가 없습니다.")
            return
    
        # '발생월'에서 '월' 문자열 제거 후 숫자형으로 변환
        filtered_df['발생월'] = filtered_df['발생월'].str.replace('월', '').astype(int)
        count_df = filtered_df.groupby(['구분2', '발생월']).size().reset_index(name='Count')
    
        if count_df.empty:
            st.warning("건수 데이터가 없습니다.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
    
        # 구분2를 x축으로, 발생월을 hue로 사용하여 라인 플롯 그리기
        sns.lineplot(data=count_df, x='구분2', y='Count', hue='발생월', marker='o', ax=ax)

        # 각 포인트에 건수 레이블 추가
        for i in range(len(count_df)):
            ax.text(count_df['구분2'].iloc[i], count_df['Count'].iloc[i], 
                    str(count_df['Count'].iloc[i]), 
                    color='black', fontsize=10, 
                    ha='center', va='bottom')

        ax.set_title('불량 부품 별 상위 10개 항목 월별 건수 분포', fontsize=16, fontproperties=font_prop)
        ax.set_xlabel('불량 부품', fontsize=14, fontproperties=font_prop)
        ax.set_ylabel('건수', fontsize=14, fontproperties=font_prop)
        st.pyplot(fig)
    


    with st.container():
        st.subheader("불량 유형 별 제품군 분포 (Heatmap)")
        if '보고 구분' in df.columns and 'E:P' in df.columns:
            pivot_table = pd.crosstab(df['보고 구분'], df['E:P'])
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5, ax=ax)
            ax.set_title('불량 유형 별 제품군 분포', fontsize=16, fontproperties=font_prop)
            ax.set_xlabel('E:P', fontsize=14, fontproperties=font_prop)
            ax.set_ylabel('보고 구분', fontsize=14, fontproperties=font_prop)
            st.pyplot(fig)
        else:
            st.write("열 '보고 구분' 또는 'E:P'이 데이터에 없습니다.")

    with st.container():
        st.subheader("담당팀 별 불량 유형 분포 (Heatmap)")
        if '담당팀' in df.columns and '보고 구분' in df.columns:
            pivot_table_team = pd.crosstab(df['담당팀'], df['보고 구분'])
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.heatmap(pivot_table_team, annot=True, fmt="d", cmap="YlOrBr", linewidths=.5, ax=ax)
            ax.set_title('담당팀 별 불량 유형 분포', fontsize=16, fontproperties=font_prop)
            ax.set_xlabel('보고 구분', fontsize=14, fontproperties=font_prop)
            ax.set_ylabel('담당팀', fontsize=14, fontproperties=font_prop)
            st.pyplot(fig)
        else:
            st.write("열 '담당팀' 또는 '보고 구분'이 데이터에 없습니다.")

def main():
    file_path = 'dashboard.csv'  # 예시: 'data.csv'
    df = load_data(file_path)
    st.write("데이터 프레임 미리보기", df.head())
    visualize_data(df)

if __name__ == '__main__':
    main()
