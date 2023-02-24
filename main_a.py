import streamlit as st
import plotly.express as px
import pandas as pd
# commit: updated comments on df Sec32

df=pd.read_csv('happy.csv')

st.title('In Search for Happiness')
xaxis=st.selectbox(label='Select the data for x-axis',
                   options=['GDP','Happiness','Generosity'])
yaxis=st.selectbox(label='Select the data for y-axis',
                   options=['GDP','Happiness','Generosity'])

st.subheader(f'{xaxis} and {yaxis}')

def get_data(x:str,y:str):
    # just need to be an array ie, list or iterable!!!
    # so doesnt need explicit list conversion!!!
    ax=list(df[x])
    ay=list(df[y])
    return(ax,ay)

x,y=get_data(xaxis.lower(),yaxis.lower())

# figure=px.line(x=x,y=y,labels={'x':xaxis,'y':yaxis})
figure=px.scatter(x=x,y=y,labels={'x':xaxis,'y':yaxis})
st.plotly_chart(figure)