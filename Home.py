import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Shilpa")
    content = '''
                Hi, I am Shilpa! I am a Data Engineer. I graduated in 2012 with a Master of Technology 
                in Computer Sciences and Engineering from Lovely Professional University Jaladhar. 
                I have worked with companies from variour industries on Data Engineering projects 
                that helped build foundational warehouses and reporting systems.
                I specialize in SQL and Python based data pipelines and database modeling.
                I have worked on setting up CDPs for QSR industry. 
                '''
    st.info(content)

content2='''
Below you can find some of the apps I have built in Python. 
Feel free to contact me!
'''

st.write(content2)

df = pd.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")