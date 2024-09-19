#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data(file_path):
    df = pd.read_excel(file_path)

    # 결측치 처리: 불량 부품 열의 결측치를 '제안'으로 대체
    if '구분2' in df.columns:
        df['구분2'] = df['구분2'].fillna('제안')
    
    return df

def visualize_data(df):
    st.title("CIQ 데이터 시각화 대시보드")

    # 발생월 별 불량 유형 분포 (violinplot으로 시각화)
    st.subheader("발생월 별 불량 유형 분포")
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x='발생월', y='보고 구분', inner="quartile", ax=ax)
    st.pyplot(fig)

    # 불량 부품 별 상위 10개 항목 분포 (barplot으로 시각화)
    st.subheader("불량 부품 별 상위 10개 항목 분포")
    top_10_parts = df['구분2'].value_counts().nlargest(10).index
    filtered_df = df[df['구분2'].isin(top_10_parts)]
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='구분2', order=top_10_parts, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

    # 불량 유형 별 제품군 분포 (heatmap으로 시각화)
    st.subheader("불량 유형 별 제품군 분포")
    pivot_table = pd.crosstab(df['보고 구분'], df['E:P'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)

    # 담당팀 별 불량 유형 (heatmap으로 시각화)
    st.subheader("담당팀 별 불량 유형 분포 (Heatmap)")
    pivot_table_team = pd.crosstab(df['담당팀'], df['보고 구분'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table_team, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)

def main():
    st.sidebar.title("엑셀 파일 업로드")
    uploaded_file = st.sidebar.file_uploader("엑셀 파일을 선택하세요", type=["xlsx"])

    if uploaded_file:
        df = load_data(uploaded_file)
        st.write("데이터 프레임 미리보기", df.head())
        visualize_data(df)
    else:
        st.write("엑셀 파일을 업로드하세요.")

if __name__ == '__main__':
    main()
