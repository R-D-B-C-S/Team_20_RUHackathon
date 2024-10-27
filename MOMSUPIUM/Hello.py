import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import csv
#from streamlit_custom_notification_box import custom_notification_box

patient_data = pd.read_csv("patient_data.csv")
#--------Url Styling-------
st.set_page_config(page_title="Hello", page_icon='🤰')
#-------Title-----------------
st.divider()
st.title("MOMSUPIUM MAIN PAGE")
st.divider()
