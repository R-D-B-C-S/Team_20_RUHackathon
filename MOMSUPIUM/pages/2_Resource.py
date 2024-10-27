import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import csv
import streamlit as st

st.markdown("# Resource Center")
st.sidebar.markdown("#Resource Center")

st.divider()
st.write("This is the Resource Center")
st.divider()
#------------Resources thata should be page 2------------

st.divider()
st.subheader("Resource Center")

#Idk why there's errors so I commented it out
#---------------------------------------------------------
data_df = pd.DataFrame({
    "Clinicians": [
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/",
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/",
        "https://www.springobgyn.com/", "https://www.springobgyn.com/"
    ],
    "Trans": [
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/",
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/",
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/",
        "https://www.nj.gov/health/fhs/wic/participants/find-wic/"
    ]  #closing trans link area
}  #data_df closing bracket
                       )  #dp.dataFrame Close
st.data_editor(
    data_df,
    column_config={
        "apps":
        st.column_config.LinkColumn(
            "Trending apps",
            help="The top trending Streamlit apps",
            validate=r"^https://[a-z]+\.streamlit\.app$",
            max_chars=100,
            display_text=r"https://(.*?)\.streamlit\.app"),
        "creator":
        st.column_config.LinkColumn("App Creator",
                                    display_text="Open profile"),
    },
    hide_index=True,
)

#---------------------------------------------------------