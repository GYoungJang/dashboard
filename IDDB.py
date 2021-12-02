import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit.elements import multiselect

st.set_page_config(page_title='Industrial_Disaster',
                    page_icon=':bar_chart:',
                    layout='wide'
                    )

df = pd.read_csv('/Users/geunyoungjang/Desktop/dashboard/df_groupby_day2.csv')


st.dataframe(df)


# #--------SIDEBAR----------
# st.sidebar.header('Filter:')
# 연도=st.sidebar.multiselect(
#     '연도 선택',
#     options=df['연도'].unique(),
#     default=df['연도'].unique()
# )

# 월=st.sidebar.multiselect(
#     '월 선택',
#     options=df['월'].unique(),
#     default=df['월'].unique()
# )

# 일=st.sidebar.multiselect(
#     '일 선택',
#     options=df['일'].unique(),
#     default=df['일'].unique()
# )

# 시간=st.sidebar.multiselect(
#     '시간 선택',
#     options=df['시간'].unique(),
#     default=df['시간'].unique()
# )

# 헬멧착용률=st.sidebar.multiselect(
#     '헬멧착용률 선택',
#     options=df['헬멧착용률'].unique(),
#     default=df['헬멧착용률'].unique()
# )

# 조끼착용률=st.sidebar.multiselect(
#     '조끼착용률 선택',
#     options=df['조끼착용률'].unique(),
#     default=df['조끼착용률'].unique()
# )

# df_selection=df.query(
#     '연도 == @연도 & 월 == @월 & 일 == @일 & 시간 == @시간 & 헬멧착용률 == @헬멧착용률 & 조끼착용률 == @조끼착용률'
# )



# # -------MAINPAGE--------
# st.title(':bar_chart:Industrial Disaster')
# st.markdown('##')

# # TOP KPI's
# 평균헬멧착용률 = round(df_selection['헬멧착용률'].mean(),1)
# 평균조끼착용률 = round(df_selection['조끼착용률'].mean(),1)

# left_column, right_column = st.columns(2)
# with left_column:
#     st.subheader('평균 헬멧착용률')
#     st.subheader(f'{평균헬멧착용률:}')
# with right_column:
#     st.subheader('평균 조끼착용률')
#     st.subheader(f'{평균조끼착용률:}')


# st.markdown('--')

# # bar chart
