import streamlit as st
import plotly.express as px
import pandas as pd
# commit: fn metadata updated Sec32

df=pd.read_csv('happy.csv')

st.title('In Search for Happiness')
xopt=st.selectbox(label='Select the data for x-axis',
                   options=['GDP','Happiness','Generosity'])
yopt=st.selectbox(label='Select the data for y-axis',
                   options=['GDP','Happiness','Generosity'])

st.subheader(f'{xopt} and {yopt}')

def get_data(opt:str)->list:
    match opt:
        case 'GDP':
            res_list=df['gdp'] # just need to be an array ie, list or iterable!!!
        case 'Happiness':
            res_list=df['happiness']
        case 'Generosity':
            res_list=df['generosity']
    return(res_list)

xarray=get_data(xopt) # just need to be an array ie, list or iterable!!!
yarray=get_data(yopt)

figure=px.scatter(x=xarray,y=yarray,labels={'x':xopt,'y':yopt})
st.plotly_chart(figure)