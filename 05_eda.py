import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown(''' 
# **Medical Exploratory Data Analysis**
This web application helps medical professionals efficiently process large medical datasets.
''')

with st.sidebar.header("Please upload your file (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_daily_case_updates/01-21-2020_2200.csv)")

if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        return pd.read_csv(uploaded_file)
    df = load_csv()
else:
    st.info('Awaiting a CSV file.')
    if st.button('Click to use example data'):
        df = pd.DataFrame(np.random.rand(100,5),
                          columns=['age','banana','orange','India','ear'])
    else:
        df = sns.load_dataset('titanic')

pr = ProfileReport(df, explorative=True)
st.header('**Input DataFrame**')
st.write(df)
st.write('---')
st.header('**Profiling Report**')
st_profile_report(pr)
