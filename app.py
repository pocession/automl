# Credits: https://github.com/nicknochnack/AutoStreamlit

import streamlit as st
import pandas as pd
import os

# import profiling capability
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# ML
from pycaret.classification import setup, compare_models, pull, save_model

with st.sidebar:
    st.image("./cell.png", width=100)
    st.title("AutoCellML")
    choice = st.radio("Navigation",["Upload","Profiling","ML","Download"])
    st.info("This application allows you to build an automated ML pipeline for cell labeling using Pycaret. It is super useful!!")

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
    st.title("Machine GO!")
    target=st.selectbox("Select Your Target",df.columns)
    if st.button("Train model"):
        setup(df,target=target,silent=True)
        setup_df = pull()
        st.info("This is the ML Experiment settings")
        st.dataframe(setup_df)
        best_model=compare_models()
        compare_df=pull()
        st.info("This is the ML Model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model, "best_model")

if choice == "Download":
   with open("best_model.pkl","rb") as f:
    st.download_button("Download the Model",f,"trained_model.pkl")