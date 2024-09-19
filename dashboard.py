#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install dash')
get_ipython().system('pip install openpyxl')


# In[1]:


import pandas as pd
from dash import Dash, dcc, html


# In[2]:


import plotly.express as px


# In[3]:


ciq='D:\\DX LV2\\ciq.xlsx'


# In[4]:


df=pd.read_excel(ciq, engine='openpyxl')


# In[5]:


df


# In[6]:


x_column = df.columns[14]


# In[8]:


fig1 = px.pie(df, names=df.columns[0], values=x_column, title=f'품질정보 유형에 따른 발생률')


# In[9]:


fig2 = px.pie(df, names=df.columns[3], values=x_column, title=f'품질정보 유형에 따른 제품군 유형')


# In[7]:


fig3 = px.bar(df, x=x_column, y=df.columns[10], title=f'품질정보 유형에 따른 불량 부품')
fig4 = px.bar(df, x=x_column, y=df.columns[13], title=f'불량 유형에 따른 담당팀')
fig5 = px.bar(df, x=x_column, y=x_column, title=f'불량 유형별 통계')


# In[10]:


app = Dash(__name__)


# In[11]:


app.layout = html.Div(children=[
    html.H1(children='Pie and Bar Chart Dashboard'),

    html.Div(children='''
        Visualizing relationships between the 5th column and other columns.
    '''),

    
    html.Div(children=[
        dcc.Graph(id='pie-chart-1', figure=fig1, style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='pie-chart-2', figure=fig2, style={'width': '48%', 'display': 'inline-block'}),
    ]),

    
    html.Div(children=[
        dcc.Graph(id='bar-chart-1', figure=fig3, style={'width': '98%', 'display': 'inline-block'}),
    ]),

    
    html.Div(children=[
        dcc.Graph(id='bar-chart-2', figure=fig4, style={'width': '98%', 'display': 'inline-block'}),
    ]),

    
    html.Div(children=[
        dcc.Graph(id='bar-chart-3', figure=fig5, style={'width': '98%', 'display': 'inline-block'}),
    ])
])


# In[12]:


if __name__ == '__main__':
    app.run_server(debug=True, port=1080)


# In[ ]:




