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
    # 2. 폰트 캐시 초기화 및 추가
    fm._rebuild()
    fm.fontManager.addfont(font_path)
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()  # matplotlib에 폰트 설정
    sns.set(font=font_prop.get_name())  # seaborn에 폰트 설정

    # 3. 설정된 폰트 확인
    st.write(f"설정된 폰트: {font_prop.get_name()}")

    # 4. CSV 파일 로드 및 대시보드 실행
    file_path = 'dashboard.csv'
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
    except FileNotFoundError:
        st.error(f"CSV 파일을 찾을 수 없습니다. '{file_path}' 파일 경로를 확인하세요.")
    else:
        # 데이터 전처리 및 시각화 코드 (생략)
        # ...
