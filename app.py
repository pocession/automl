import streamlit as st
import pandas as pd
import os

# import profiling capability
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


with st.sidebar:
    st.image("./cell.png")
    st.title("AutoCellML")
    choice = st.radio("Navigation",["Upload","Profiling","ML","Download"])
    st.info("This application allows you to build an automated ML pipeline for cell labeling using Streamlit, Pandas profiling, and Pycaret. It is super useful!!")


if os.path.exists("sourcedata.csv"):
    df=pd.read_csv("sourcedata.csv",index_col=None)

if choice == "Upload":
    st.title("Upload Your Data for Modeling!")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv",index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)

if choice == "ML":
    pass

if choice == "Download":
    pass