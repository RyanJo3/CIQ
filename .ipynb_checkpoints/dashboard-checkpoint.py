{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c9d488d1-79e7-4dcf-9246-72d7e818328c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pandas\n",
      "  Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl.metadata (19 kB)\n",
      "Collecting numpy>=1.26.0 (from pandas)\n",
      "  Downloading numpy-2.1.1-cp312-cp312-win_amd64.whl.metadata (59 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Collecting pytz>=2020.1 (from pandas)\n",
      "  Downloading pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)\n",
      "Collecting tzdata>=2022.7 (from pandas)\n",
      "  Downloading tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl (11.5 MB)\n",
      "   ---------------------------------------- 0.0/11.5 MB ? eta -:--:--\n",
      "   ---------------------------------------  11.3/11.5 MB 78.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 11.5/11.5 MB 48.0 MB/s eta 0:00:00\n",
      "Downloading numpy-2.1.1-cp312-cp312-win_amd64.whl (12.6 MB)\n",
      "   ---------------------------------------- 0.0/12.6 MB ? eta -:--:--\n",
      "   ---------------------------------------  12.3/12.6 MB 64.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 12.6/12.6 MB 46.3 MB/s eta 0:00:00\n",
      "Downloading pytz-2024.2-py2.py3-none-any.whl (508 kB)\n",
      "Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)\n",
      "Installing collected packages: pytz, tzdata, numpy, pandas\n",
      "Successfully installed numpy-2.1.1 pandas-2.2.2 pytz-2024.2 tzdata-2024.1\n",
      "Collecting dash\n",
      "  Downloading dash-2.18.1-py3-none-any.whl.metadata (10 kB)\n",
      "Collecting Flask<3.1,>=1.0.4 (from dash)\n",
      "  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)\n",
      "Collecting Werkzeug<3.1 (from dash)\n",
      "  Downloading werkzeug-3.0.4-py3-none-any.whl.metadata (3.7 kB)\n",
      "Collecting plotly>=5.0.0 (from dash)\n",
      "  Downloading plotly-5.24.1-py3-none-any.whl.metadata (7.3 kB)\n",
      "Collecting dash-html-components==2.0.0 (from dash)\n",
      "  Downloading dash_html_components-2.0.0-py3-none-any.whl.metadata (3.8 kB)\n",
      "Collecting dash-core-components==2.0.0 (from dash)\n",
      "  Downloading dash_core_components-2.0.0-py3-none-any.whl.metadata (2.9 kB)\n",
      "Collecting dash-table==5.0.0 (from dash)\n",
      "  Downloading dash_table-5.0.0-py3-none-any.whl.metadata (2.4 kB)\n",
      "Collecting importlib-metadata (from dash)\n",
      "  Downloading importlib_metadata-8.5.0-py3-none-any.whl.metadata (4.8 kB)\n",
      "Collecting typing-extensions>=4.1.1 (from dash)\n",
      "  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)\n",
      "Requirement already satisfied: requests in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from dash) (2.32.3)\n",
      "Collecting retrying (from dash)\n",
      "  Downloading retrying-1.3.4-py3-none-any.whl.metadata (6.9 kB)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from dash) (1.6.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from dash) (74.1.2)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.1.4)\n",
      "Collecting itsdangerous>=2.1.2 (from Flask<3.1,>=1.0.4->dash)\n",
      "  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting click>=8.1.3 (from Flask<3.1,>=1.0.4->dash)\n",
      "  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)\n",
      "Collecting blinker>=1.6.2 (from Flask<3.1,>=1.0.4->dash)\n",
      "  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting tenacity>=6.2.0 (from plotly>=5.0.0->dash)\n",
      "  Downloading tenacity-9.0.0-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: packaging in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from plotly>=5.0.0->dash) (24.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from Werkzeug<3.1->dash) (2.1.5)\n",
      "Collecting zipp>=3.20 (from importlib-metadata->dash)\n",
      "  Downloading zipp-3.20.2-py3-none-any.whl.metadata (3.7 kB)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests->dash) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests->dash) (3.9)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests->dash) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests->dash) (2024.8.30)\n",
      "Requirement already satisfied: six>=1.7.0 in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from retrying->dash) (1.16.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\hyuntae.jo\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click>=8.1.3->Flask<3.1,>=1.0.4->dash) (0.4.6)\n",
      "Downloading dash-2.18.1-py3-none-any.whl (7.5 MB)\n",
      "   ---------------------------------------- 0.0/7.5 MB ? eta -:--:--\n",
      "   ---------------------------------------- 7.5/7.5 MB 42.3 MB/s eta 0:00:00\n",
      "Downloading dash_core_components-2.0.0-py3-none-any.whl (3.8 kB)\n",
      "Downloading dash_html_components-2.0.0-py3-none-any.whl (4.1 kB)\n",
      "Downloading dash_table-5.0.0-py3-none-any.whl (3.9 kB)\n",
      "Downloading flask-3.0.3-py3-none-any.whl (101 kB)\n",
      "Downloading plotly-5.24.1-py3-none-any.whl (19.1 MB)\n",
      "   ---------------------------------------- 0.0/19.1 MB ? eta -:--:--\n",
      "   ------------------------------ --------- 14.4/19.1 MB 69.7 MB/s eta 0:00:01\n",
      "   ---------------------------------------  18.9/19.1 MB 70.2 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 19.1/19.1 MB 44.5 MB/s eta 0:00:00\n",
      "Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)\n",
      "Downloading werkzeug-3.0.4-py3-none-any.whl (227 kB)\n",
      "Downloading importlib_metadata-8.5.0-py3-none-any.whl (26 kB)\n",
      "Downloading retrying-1.3.4-py3-none-any.whl (11 kB)\n",
      "Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)\n",
      "Downloading click-8.1.7-py3-none-any.whl (97 kB)\n",
      "Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)\n",
      "Downloading tenacity-9.0.0-py3-none-any.whl (28 kB)\n",
      "Downloading zipp-3.20.2-py3-none-any.whl (9.2 kB)\n",
      "Installing collected packages: dash-table, dash-html-components, dash-core-components, zipp, Werkzeug, typing-extensions, tenacity, retrying, itsdangerous, click, blinker, plotly, importlib-metadata, Flask, dash\n",
      "Successfully installed Flask-3.0.3 Werkzeug-3.0.4 blinker-1.8.2 click-8.1.7 dash-2.18.1 dash-core-components-2.0.0 dash-html-components-2.0.0 dash-table-5.0.0 importlib-metadata-8.5.0 itsdangerous-2.2.0 plotly-5.24.1 retrying-1.3.4 tenacity-9.0.0 typing-extensions-4.12.2 zipp-3.20.2\n",
      "Collecting openpyxl\n",
      "  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)\n",
      "Collecting et-xmlfile (from openpyxl)\n",
      "  Downloading et_xmlfile-1.1.0-py3-none-any.whl.metadata (1.8 kB)\n",
      "Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)\n",
      "Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)\n",
      "Installing collected packages: et-xmlfile, openpyxl\n",
      "Successfully installed et-xmlfile-1.1.0 openpyxl-3.1.5\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas\n",
    "!pip install dash\n",
    "!pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58b7fead-8918-49c5-acf4-3d3cb2f2d466",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from dash import Dash, dcc, html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9999b65d-04b0-46ed-841d-eea6e1b38863",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0b5441d0-9889-4586-93de-86fbdcd92eb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "ciq='D:\\\\DX LV2\\\\ciq.xlsx'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "496cab5e-f489-4aeb-817b-1d6ffb5f5582",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_excel(ciq, engine='openpyxl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c89a77c2-8498-4dd0-a28a-3c23375f398d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>발생월</th>\n",
       "      <th>주차</th>\n",
       "      <th>구분</th>\n",
       "      <th>E:P</th>\n",
       "      <th>모델명</th>\n",
       "      <th>일련번호</th>\n",
       "      <th>제목</th>\n",
       "      <th>내용(비고)</th>\n",
       "      <th>제조번호</th>\n",
       "      <th>구분1</th>\n",
       "      <th>구분2</th>\n",
       "      <th>구분3</th>\n",
       "      <th>구분 상세</th>\n",
       "      <th>담당팀</th>\n",
       "      <th>보고 구분</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1월</td>\n",
       "      <td>1주차</td>\n",
       "      <td>240102최형철01</td>\n",
       "      <td>068.멀티V</td>\n",
       "      <td>RPUW18BX9M.AKM</td>\n",
       "      <td>20240157973</td>\n",
       "      <td>품질정보-240102최형철01-멀티브이-RPUW18BX9M-실외기 시운전시 43번 ...</td>\n",
       "      <td>■ 현상 및 문제점    - 시운전시 43번 발생 확인 ■ 원인(추정 원인</td>\n",
       "      <td>310TATGDB513</td>\n",
       "      <td>부품</td>\n",
       "      <td>센서</td>\n",
       "      <td>CH43</td>\n",
       "      <td>고압센서 불량으로 CH43 발생</td>\n",
       "      <td>모듈러개발3팀</td>\n",
       "      <td>기구</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1월</td>\n",
       "      <td>1주차</td>\n",
       "      <td>240102한영범01</td>\n",
       "      <td>068.멀티V</td>\n",
       "      <td>GPUW251C2SM.AKM</td>\n",
       "      <td>20240157976</td>\n",
       "      <td>품질정보-240102한영범01-GHP-GPUW251C2SM-172번에러 발생 SMP...</td>\n",
       "      <td>■ 현상 및 문제점 -전원투입후 실외기 172번 에러 발생(오일유압스위치 이상)  ...</td>\n",
       "      <td>310KCCV0K315</td>\n",
       "      <td>부품</td>\n",
       "      <td>PCB</td>\n",
       "      <td>ch172</td>\n",
       "      <td>smps불량</td>\n",
       "      <td>GHP</td>\n",
       "      <td>기구</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1월</td>\n",
       "      <td>1주차</td>\n",
       "      <td>240102윤재영01</td>\n",
       "      <td>071.상업용스탠드</td>\n",
       "      <td>PNW1453T9FR.AKM</td>\n",
       "      <td>20240157975</td>\n",
       "      <td>품질정보-240102윤재영01-상업용스탠드-PNW1453T9FR-실내기 가동 중 떨...</td>\n",
       "      <td>■ 현상 및 문제점 :   -시운전 중 실내기 측 소음 발생으로 지원 요청 ■ 점검...</td>\n",
       "      <td>310KCLH0US44</td>\n",
       "      <td>소음</td>\n",
       "      <td>팬모터</td>\n",
       "      <td>소음</td>\n",
       "      <td>팬모터 소음</td>\n",
       "      <td>모듈러개발3팀</td>\n",
       "      <td>기구</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1월</td>\n",
       "      <td>1주차</td>\n",
       "      <td>230102최세진01</td>\n",
       "      <td>068.멀티V</td>\n",
       "      <td>RPUW14GX9E.AKM</td>\n",
       "      <td>20240157977</td>\n",
       "      <td>품질정보-230102최세진01-멀티브이-RPUW26GX9E-자동시운전리포트와 LGM...</td>\n",
       "      <td>■ 현상 및 문제점 LGMV(PC, Mobile)와 자동시운전보고서 표기값 상이  ...</td>\n",
       "      <td>308KCHE0LW05</td>\n",
       "      <td>시운전</td>\n",
       "      <td>LGMV</td>\n",
       "      <td>표기값 오류</td>\n",
       "      <td>LGMV와 시운전보고서 표기값 상이</td>\n",
       "      <td>사이클로직</td>\n",
       "      <td>제어SW</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1월</td>\n",
       "      <td>1주차</td>\n",
       "      <td>240102한영범02</td>\n",
       "      <td>068.멀티V</td>\n",
       "      <td>RPUW14BX9P.AKM</td>\n",
       "      <td>20240157978</td>\n",
       "      <td>품질정보-240102한영범02-멀티브이-RPUW14BX9P-천진산 실외기 104 에...</td>\n",
       "      <td>■ 현상 및 문제점 -천진산 실외기 조합 설치시 104에러 (실외기간 통신에러) 발...</td>\n",
       "      <td>308TAFZER571</td>\n",
       "      <td>부품</td>\n",
       "      <td>PCB</td>\n",
       "      <td>CH104</td>\n",
       "      <td>천진산 PCB 조합 CH104 에러</td>\n",
       "      <td>HW개발1팀</td>\n",
       "      <td>제어HW</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1296</th>\n",
       "      <td>8월</td>\n",
       "      <td>5주차</td>\n",
       "      <td>240830김두섭01</td>\n",
       "      <td>038.상업용스탠드</td>\n",
       "      <td>PNW2900F9SF.AKM</td>\n",
       "      <td>20240863896</td>\n",
       "      <td>품질정보-240830김두섭01-상업용스탠드-PNW2900F9SF-상업용 스탠드 Wi...</td>\n",
       "      <td>■ 현상 및 문제점   - 10마력 상업용 스탠드 설치 현장에서 Wi-Fi 모듈을 ...</td>\n",
       "      <td>407KCYQ22N94</td>\n",
       "      <td>제안</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>싱글 CAC</td>\n",
       "      <td>제안</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1297</th>\n",
       "      <td>8월</td>\n",
       "      <td>5주차</td>\n",
       "      <td>240830석재봉01</td>\n",
       "      <td>035.멀티V</td>\n",
       "      <td>RNW0520A2U.AKM</td>\n",
       "      <td>20240863898</td>\n",
       "      <td>품질정보-240830석재봉01-멀티브이-RNW0520A2U-프런트판넬 크리스탈 루버...</td>\n",
       "      <td>■ 현상 및 문제점   - 시운전 진행중 프론트 판넬 루버 1EA 작동 안됨</td>\n",
       "      <td>406KCMR05R95</td>\n",
       "      <td>부품</td>\n",
       "      <td>프론트판넬</td>\n",
       "      <td>루버 동작 불량</td>\n",
       "      <td>4WAY 크리스탈 베인 동작 불량</td>\n",
       "      <td>SQA</td>\n",
       "      <td>협력사</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1298</th>\n",
       "      <td>8월</td>\n",
       "      <td>5주차</td>\n",
       "      <td>240731이재동01</td>\n",
       "      <td>035.멀티V</td>\n",
       "      <td>RNW0600A2U.AKM</td>\n",
       "      <td>20240863902</td>\n",
       "      <td>품질정보-240731이재동01 -멀티브이-실내기판넬하네스불량발생- 판넬교체</td>\n",
       "      <td>■ 현상 및 문제점 -시운전 전 프론트판넬 커넥터 중 1개소 불량으로 CIQ지원요청...</td>\n",
       "      <td>406KCZP0TK25</td>\n",
       "      <td>부품</td>\n",
       "      <td>프론트판넬</td>\n",
       "      <td>커넥터 누락</td>\n",
       "      <td>4WAY 프론트 판넬 커넥터 누락</td>\n",
       "      <td>SQA</td>\n",
       "      <td>협력사</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1299</th>\n",
       "      <td>8월</td>\n",
       "      <td>5주차</td>\n",
       "      <td>240830김정진01</td>\n",
       "      <td>036.카세트/덕트</td>\n",
       "      <td>UUW145039FR.AKM</td>\n",
       "      <td>20240863903</td>\n",
       "      <td>품질정보-240830김정진01-싱글카세트-UUW145039FR-실외기 COMP압축불...</td>\n",
       "      <td>■ 현상 및 문제점 - 시운전 진행 5일후 냉방약 발생함 ■ 점검사항</td>\n",
       "      <td>405TADRHJ210</td>\n",
       "      <td>부품</td>\n",
       "      <td>컴프레셔</td>\n",
       "      <td>냉방약</td>\n",
       "      <td>실외기 컴프레셔 불량</td>\n",
       "      <td>부품솔루션</td>\n",
       "      <td>기구</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1300</th>\n",
       "      <td>8월</td>\n",
       "      <td>5주차</td>\n",
       "      <td>240830이재동02</td>\n",
       "      <td>035.멀티V</td>\n",
       "      <td>RPUW241X9H.AKM</td>\n",
       "      <td>20240863914</td>\n",
       "      <td>품질정보-240830이재동02-멀티브이-RPUW241X9H-실외기 오일 세퍼레이트로...</td>\n",
       "      <td>■ 현상 및 문제점 : - 시운전 완료 후 일주일만에 입주한 상가 제품 가동 중 냉...</td>\n",
       "      <td>407KCFT19467</td>\n",
       "      <td>누설</td>\n",
       "      <td>파이프</td>\n",
       "      <td>냉매 누설</td>\n",
       "      <td>실외기 오일 세퍼레이터 배관 용접부위 터짐</td>\n",
       "      <td>제조</td>\n",
       "      <td>제조</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1301 rows × 15 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      발생월   주차            구분         E:P              모델명         일련번호  \\\n",
       "0      1월  1주차   240102최형철01     068.멀티V   RPUW18BX9M.AKM  20240157973   \n",
       "1      1월  1주차   240102한영범01     068.멀티V  GPUW251C2SM.AKM  20240157976   \n",
       "2      1월  1주차   240102윤재영01  071.상업용스탠드  PNW1453T9FR.AKM  20240157975   \n",
       "3      1월  1주차   230102최세진01     068.멀티V   RPUW14GX9E.AKM  20240157977   \n",
       "4      1월  1주차   240102한영범02     068.멀티V   RPUW14BX9P.AKM  20240157978   \n",
       "...   ...  ...           ...         ...              ...          ...   \n",
       "1296   8월  5주차   240830김두섭01  038.상업용스탠드  PNW2900F9SF.AKM  20240863896   \n",
       "1297   8월  5주차   240830석재봉01     035.멀티V   RNW0520A2U.AKM  20240863898   \n",
       "1298   8월  5주차  240731이재동01      035.멀티V   RNW0600A2U.AKM  20240863902   \n",
       "1299   8월  5주차   240830김정진01  036.카세트/덕트  UUW145039FR.AKM  20240863903   \n",
       "1300   8월  5주차   240830이재동02     035.멀티V   RPUW241X9H.AKM  20240863914   \n",
       "\n",
       "                                                     제목  \\\n",
       "0     품질정보-240102최형철01-멀티브이-RPUW18BX9M-실외기 시운전시 43번 ...   \n",
       "1     품질정보-240102한영범01-GHP-GPUW251C2SM-172번에러 발생 SMP...   \n",
       "2     품질정보-240102윤재영01-상업용스탠드-PNW1453T9FR-실내기 가동 중 떨...   \n",
       "3     품질정보-230102최세진01-멀티브이-RPUW26GX9E-자동시운전리포트와 LGM...   \n",
       "4     품질정보-240102한영범02-멀티브이-RPUW14BX9P-천진산 실외기 104 에...   \n",
       "...                                                 ...   \n",
       "1296  품질정보-240830김두섭01-상업용스탠드-PNW2900F9SF-상업용 스탠드 Wi...   \n",
       "1297  품질정보-240830석재봉01-멀티브이-RNW0520A2U-프런트판넬 크리스탈 루버...   \n",
       "1298          품질정보-240731이재동01 -멀티브이-실내기판넬하네스불량발생- 판넬교체   \n",
       "1299  품질정보-240830김정진01-싱글카세트-UUW145039FR-실외기 COMP압축불...   \n",
       "1300  품질정보-240830이재동02-멀티브이-RPUW241X9H-실외기 오일 세퍼레이트로...   \n",
       "\n",
       "                                                 내용(비고)          제조번호  구분1  \\\n",
       "0             ■ 현상 및 문제점    - 시운전시 43번 발생 확인 ■ 원인(추정 원인  310TATGDB513   부품   \n",
       "1     ■ 현상 및 문제점 -전원투입후 실외기 172번 에러 발생(오일유압스위치 이상)  ...  310KCCV0K315   부품   \n",
       "2     ■ 현상 및 문제점 :   -시운전 중 실내기 측 소음 발생으로 지원 요청 ■ 점검...  310KCLH0US44   소음   \n",
       "3     ■ 현상 및 문제점 LGMV(PC, Mobile)와 자동시운전보고서 표기값 상이  ...  308KCHE0LW05  시운전   \n",
       "4     ■ 현상 및 문제점 -천진산 실외기 조합 설치시 104에러 (실외기간 통신에러) 발...  308TAFZER571   부품   \n",
       "...                                                 ...           ...  ...   \n",
       "1296  ■ 현상 및 문제점   - 10마력 상업용 스탠드 설치 현장에서 Wi-Fi 모듈을 ...  407KCYQ22N94   제안   \n",
       "1297         ■ 현상 및 문제점   - 시운전 진행중 프론트 판넬 루버 1EA 작동 안됨  406KCMR05R95   부품   \n",
       "1298  ■ 현상 및 문제점 -시운전 전 프론트판넬 커넥터 중 1개소 불량으로 CIQ지원요청...  406KCZP0TK25   부품   \n",
       "1299             ■ 현상 및 문제점 - 시운전 진행 5일후 냉방약 발생함 ■ 점검사항  405TADRHJ210   부품   \n",
       "1300  ■ 현상 및 문제점 : - 시운전 완료 후 일주일만에 입주한 상가 제품 가동 중 냉...  407KCFT19467   누설   \n",
       "\n",
       "        구분2       구분3                    구분 상세      담당팀 보고 구분  \n",
       "0        센서      CH43        고압센서 불량으로 CH43 발생  모듈러개발3팀    기구  \n",
       "1       PCB     ch172                   smps불량      GHP    기구  \n",
       "2       팬모터        소음                   팬모터 소음  모듈러개발3팀    기구  \n",
       "3      LGMV    표기값 오류      LGMV와 시운전보고서 표기값 상이    사이클로직  제어SW  \n",
       "4       PCB     CH104      천진산 PCB 조합 CH104 에러   HW개발1팀  제어HW  \n",
       "...     ...       ...                      ...      ...   ...  \n",
       "1296    NaN       NaN                      NaN   싱글 CAC    제안  \n",
       "1297  프론트판넬  루버 동작 불량       4WAY 크리스탈 베인 동작 불량      SQA   협력사  \n",
       "1298  프론트판넬    커넥터 누락       4WAY 프론트 판넬 커넥터 누락      SQA   협력사  \n",
       "1299   컴프레셔       냉방약              실외기 컴프레셔 불량    부품솔루션    기구  \n",
       "1300    파이프     냉매 누설  실외기 오일 세퍼레이터 배관 용접부위 터짐       제조    제조  \n",
       "\n",
       "[1301 rows x 15 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b8ec8ef3-8e91-4226-973a-4044555d9b99",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_column = df.columns[14]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f0bff438-581c-4f62-90b9-6c78a18c7d4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig1 = px.pie(df, names=df.columns[0], values=x_column, title=f'품질정보 유형에 따른 발생률')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8ffec486-60bf-4bc1-b886-aac2d77f5c48",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig2 = px.pie(df, names=df.columns[3], values=x_column, title=f'품질정보 유형에 따른 제품군 유형')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ccb0f9d0-b8fd-4637-a423-812a77f8fabc",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig3 = px.bar(df, x=x_column, y=df.columns[10], title=f'품질정보 유형에 따른 불량 부품')\n",
    "fig4 = px.bar(df, x=x_column, y=df.columns[13], title=f'불량 유형에 따른 담당팀')\n",
    "fig5 = px.bar(df, x=x_column, y=x_column, title=f'불량 유형별 통계')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cae217ff-4b25-47b6-b8ab-333473a396a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Dash(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f32c580d-3f3c-459d-bc5b-40aeab09c83b",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout = html.Div(children=[\n",
    "    html.H1(children='Pie and Bar Chart Dashboard'),\n",
    "\n",
    "    html.Div(children='''\n",
    "        Visualizing relationships between the 5th column and other columns.\n",
    "    '''),\n",
    "\n",
    "    \n",
    "    html.Div(children=[\n",
    "        dcc.Graph(id='pie-chart-1', figure=fig1, style={'width': '48%', 'display': 'inline-block'}),\n",
    "        dcc.Graph(id='pie-chart-2', figure=fig2, style={'width': '48%', 'display': 'inline-block'}),\n",
    "    ]),\n",
    "\n",
    "    \n",
    "    html.Div(children=[\n",
    "        dcc.Graph(id='bar-chart-1', figure=fig3, style={'width': '98%', 'display': 'inline-block'}),\n",
    "    ]),\n",
    "\n",
    "    \n",
    "    html.Div(children=[\n",
    "        dcc.Graph(id='bar-chart-2', figure=fig4, style={'width': '98%', 'display': 'inline-block'}),\n",
    "    ]),\n",
    "\n",
    "    \n",
    "    html.Div(children=[\n",
    "        dcc.Graph(id='bar-chart-3', figure=fig5, style={'width': '98%', 'display': 'inline-block'}),\n",
    "    ])\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "164d7f53-f4ec-4625-adc8-78f87bd29bb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:1080/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x13c8ea3ac60>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True, port=1080)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97f70c95-8d38-4343-a2d8-44c62b247d6d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
