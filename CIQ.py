#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# In[5]:


def load_data(file_path):
    df = pd.read_excel(file_path)

    # 결측치 처리: 불량 부품 열의 결측치를 '제안'으로 대체
    if '불량 부품' in df.columns:
        df['불량 부품'] = df['불량 부품'].fillna('제안')
    
    return df


# In[6]:


def visualize_data(df):
    st.title("CIQ 데이터 시각화 대시보드")

    # 발생월 별 불량 유형 분포 (violinplot으로 시각화)
    st.subheader("발생월 별 불량 유형 분포")
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x='발생월', y='보고 구분', inner="quartile", ax=ax)
    st.pyplot(fig)

    # 불량 부품 별 분포 (catplot으로 시각화)
    st.subheader("불량 부품 별 분포")
    fig = sns.catplot(data=df, x='구분2', kind="count", height=5, aspect=2)
    st.pyplot(fig)

    # 불량 유형 별 제품군 분포 (pointplot으로 시각화)
    st.subheader("불량 유형 별 제품군 분포")
    fig, ax = plt.subplots()
    sns.pointplot(data=df, x='보고 구분', y='E:P', ax=ax)
    st.pyplot(fig)

    # 담당팀 별 불량 유형 (heatmap으로 시각화)
    st.subheader("담당팀 별 불량 유형 분포 (Heatmap)")
    pivot_table = pd.crosstab(df['담당팀'], df['보고 구분'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)


# In[7]:


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

