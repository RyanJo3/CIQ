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
    df = pd.read_csv(file_path)
    if '구분2' in df.columns:
        df['구분2'] = df['구분2'].fillna('제안')
    return df

def visualize_data(df):
    st.title("CIQ 데이터 시각화 대시보드")

    col1 = st.columns(1)

    with col1:
        st.subheader("발생월 별 불량 유형 분포 (Boxplot)")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='발생월', y='보고 구분', palette='Set3', ax=ax)
        ax.set_title('발생월 별 불량 유형 분포', fontsize=16, fontproperties=font_prop)
        ax.set_xlabel('발생월', fontsize=14, fontproperties=font_prop)
        ax.set_ylabel('보고 구분', fontsize=14, fontproperties=font_prop)
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
