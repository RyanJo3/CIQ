#!/usr/bin/env python
# coding: utf-8







# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.font_manager as fm
import os

def set_korean_font():
    font_path = 'NanumGothic.ttf'
    if os.path.exists(font_path):
        font_properties = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_properties.get_name()
        print(f"'{font_properties.get_name()}' 폰트가 성공적으로 설정되었습니다.")
    else:
        plt.rcParams['font.family'] = 'Arial'
        print("폰트 파일을 찾을 수 없습니다. 기본 폰트로 설정합니다.")
    plt.rcParams['axes.unicode_minus'] = False

set_korean_font()

# 엑셀 파일 경로 지정
file_path = "D:\\DX LV2\\CIQDASHBOARD.xlsx"

# 데이터 불러오기
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        if '구분2' in df.columns:
            df['구분2'] = df['구분2'].fillna('제안')
        return df
    except Exception as e:
        st.write(f"파일을 불러오는 중 오류가 발생했습니다: {e}")
        return None

# 데이터 시각화
def visualize_data(df):
    st.title("CIQ 데이터 시각화 대시보드")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("발생월 별 불량 유형 분포 (Boxplot)")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='발생월', y='보고 구분', palette='Set3', ax=ax)
        ax.set_title('발생월 별 불량 유형 분포', fontsize=16)
        ax.set_xlabel('발생월', fontsize=14)
        ax.set_ylabel('보고 구분', fontsize=14)
        st.pyplot(fig)

    with col2:
        st.subheader("불량 부품 별 상위 10개 항목 분포 (Barplot)")
        top_10_parts = df['구분2'].value_counts().nlargest(10).index
        filtered_df = df[df['구분2'].isin(top_10_parts)]
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=filtered_df, x='구분2', y='발생월', estimator=lambda x: len(x) / len(filtered_df) * 100, palette='coolwarm', order=top_10_parts, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.set_title('불량 부품 별 상위 10개 항목 분포', fontsize=16)
        ax.set_xlabel('불량 부품', fontsize=14)
        ax.set_ylabel('비율 (%)', fontsize=14)
        st.pyplot(fig)

    with st.container():
        st.subheader("불량 유형 별 제품군 분포 (Heatmap)")
        if '보고 구분' in df.columns and 'E:P' in df.columns:
            pivot_table = pd.crosstab(df['보고 구분'], df['E:P'])
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5, ax=ax)
            ax.set_title('불량 유형 별 제품군 분포', fontsize=16)
            ax.set_xlabel('E:P', fontsize=14)
            ax.set_ylabel('보고 구분', fontsize=14)
            st.pyplot(fig)
        else:
            st.write("열 '보고 구분' 또는 'E:P'이 데이터에 없습니다.")

    with st.container():
        st.subheader("담당팀 별 불량 유형 분포 (Heatmap)")
        if '담당팀' in df.columns and '보고 구분' in df.columns:
            pivot_table_team = pd.crosstab(df['담당팀'], df['보고 구분'])
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.heatmap(pivot_table_team, annot=True, fmt="d", cmap="YlOrBr", linewidths=.5, ax=ax)
            ax.set_title('담당팀 별 불량 유형 분포', fontsize=16)
            ax.set_xlabel('보고 구분', fontsize=14)
            ax.set_ylabel('담당팀', fontsize=14)
            st.pyplot(fig)
        else:
            st.write("열 '담당팀' 또는 '보고 구분'이 데이터에 없습니다.")

# Streamlit 앱 메인 함수
def main():
    st.sidebar.title("엑셀 파일 자동 로드")
    st.write(f"파일 경로: {file_path}")  # 파일 경로 출력
    if os.path.exists(file_path):
        st.write("파일이 존재합니다.")
        df = load_data(file_path)
        if df is not None:
            st.write("데이터 프레임 미리보기", df.head())
            visualize_data(df)
        else:
            st.write("데이터를 불러오는 중 오류가 발생했습니다.")
    else:
        st.write("지정된 경로에 엑셀 파일이 없습니다.")

if __name__ == '__main__':
    main()
