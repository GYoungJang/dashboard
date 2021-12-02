import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit.elements import multiselect, plotly_chart

st.set_page_config(page_title='안전장비 착용률',
                    page_icon=':bar_chart:',
                    layout='wide'
                    )



df = pd.read_csv('/Users/geunyoungjang/Desktop/dashboard/통계.csv')




#--------SIDEBAR----------
st.sidebar.header('FILTER')
연도=st.sidebar.multiselect(
    '연도 선택',
    options=df['연도'].unique(),
    default=df['연도'].unique()
    )

월=st.sidebar.multiselect(
    '월 선택',
    options=df['월'].unique(),
    default=df['월'].unique()
    )

일=st.sidebar.multiselect(
    '일 선택',
    options=df['일'].unique(),
    default=df['일'].unique()
)

# 헬멧착용률=st.sidebar.multiselect(
#     '헬멧착용률 선택',
#     options=df['헬멧착용률'].unique()
# )

# 조끼착용률=st.sidebar.multiselect(
#     '조끼착용률 선택',
#     options=df['조끼착용률'].unique()
#     )

df_selection=df.query(
    '연도 == @연도 & 월 == @월 & 일 == @일'
)

# st.dataframe(df_selection)

# -------MAINPAGE--------
st.title(':bar_chart:안전장비 착용률')
st.markdown('##')

# TOP KPI's
평균헬멧착용률 = round(df_selection['헬멧착용률'].mean(),1)
평균조끼착용률 = round(df_selection['조끼착용률'].mean(),1)
별표1 = ":star:" * int(round(평균헬멧착용률/10,0))
별표2 = ":star:" * int(round(평균조끼착용률/10,0))

left_column, right_column = st.columns(2)
with left_column:
    st.subheader('평균 헬멧착용률') 
    st.subheader(f'{평균헬멧착용률}% {별표1}')
with right_column:
    st.subheader('평균 조끼착용률')
    st.subheader(f'{평균조끼착용률}% {별표2}')


st.markdown('---')

# helmet bar chart
monthly_average_helmet = (
    df_selection.groupby(['월']).mean()[['헬멧착용률']]
)

fig_helmet = px.bar(
    monthly_average_helmet,
    x='헬멧착용률',
    y=monthly_average_helmet.index,
    orientation='h',
    title = '<b>월별 헬멧착용률</b>',
    color_discrete_sequence=['#0083B8']*len(monthly_average_helmet),
    template='plotly_white',
)
fig_helmet.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False))
)

# st.plotly_chart(fig_helmet)

# vest bar chart
monthly_average_vest = (
    df_selection.groupby(['월']).mean()[['조끼착용률']]
)

fig_vest = px.bar(
    monthly_average_vest,
    x=monthly_average_vest.index,
    y='조끼착용률',
    title = '<b>월별 조끼착용률</b>',
    color_discrete_sequence=['#0083B8']*len(monthly_average_vest),
    template='plotly_white',
)

fig_vest.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
)

# st.plotly_chart(fig_vest)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_helmet, use_container_width=True)
right_column.plotly_chart(fig_vest, use_container_width=True)

#---------HIDE STREAMLIT STYLE ----------
hide_st_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                '''
st.markdown(hide_st_style, unsafe_allow_html=True)