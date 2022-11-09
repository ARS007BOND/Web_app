from doctest import Example
import profile
from re import A
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# web app ttile
st.markdown(''' 
# **Medical Exploratory Data Analysis**
This web application has been designed to aid meidical professionals in effieciently process large medical databases.

''')

#  uploading a file from pc

with st.sidebar.header("Please upload your file (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_daily_case_updates/01-21-2020_2200.csv)")

#profiling report for panda

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative= True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for a csv file.')
    if st.button('Click to use example data'):
       #example dataset

        def load_data():
            a = pd.DataFrame( np.random.rand(100,5),
                                columns=['age','banana','orange', 'India','ear']) 
            return a 
        df = load_data()
        pr = ProfileReport(df, explorative= True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)
        

