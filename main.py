import streamlit as st
import plotly.express as px
import pandas as pd
# commit: better opt record handling Sec32

df=pd.read_csv('happy.csv')

st.title('In Search for Happiness')
xopt=st.selectbox(label='Select the data for x-axis',
                   options=['GDP','Happiness','Generosity'])
yopt=st.selectbox(label='Select the data for y-axis',
                   options=['GDP','Happiness','Generosity'])

st.subheader(f'{xopt} and {yopt}')

def get_data(opt:str):
    match opt:
        case 'GDP':
            res_list=df['gdp']
        case 'Happiness':
            res_list=df['happiness']
        case 'Generosity':
            res_list=df['generosity']
    return(res_list)

x=get_data(xopt)
y=get_data(yopt)

figure=px.scatter(x=x,y=y,labels={'x':xopt,'y':yopt})
st.plotly_chart(figure)