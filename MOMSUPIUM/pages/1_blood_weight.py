import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import csv
#from streamlit_custom_notification_box import custom_notification_box

st.markdown("Data Entry")
st.sidebar.markdown("Data Entry")

patient_data = pd.read_csv("patient_data.csv")
#--------Url Styling-------
#st.set_page_config(page_title='Momsupium', page_icon='🤰')
#-------Title-----------------
st.title("MOMSUPIUM")
st.divider()
#Data reading
last_values = patient_data.iloc[-1]
#if datetime.strptime(last_values["Date"],"%m/%d/%Y") -(datetime.now()) >= timedelta(days=7):


#------------Name--------------------------
nam = st.text_input("Enter your Name")

#----------weight---------------------------
weight = st.number_input("Enter your Weight")
st.write("You entered: ", weight)

if last_values["Weight (lbs)"] - weight <= 5:
    st.error(f"Warning: The input value {weight} indicates that you have gained 5 pounds or more within the span of a week, this is a risk factor for pre-eclampsia please contact a medical professional for the best next steps!")
else:
    st.write(f"Thank you for documenting your weight with us today.")



#----------urine level-----------------------
Protein_level = st.selectbox(
    "Enter your Protein Urine level",
    ("-", " +/-", "1+", "2+", "3+", "4+"),
    index=None,
    placeholder="Select a Protein level...",
)
st.write("You selected:", Protein_level)
#----------blood pressure-----------------------
bp_Systolic = st.number_input("Enter your Systolic Blood Pressure. (The Top number on your blood pressure chart)")


bp_Diastolic = st.number_input("Enter your Diastolic Blood Pressure. (The Bottom number on your blood pressure chart)")
#st.write("You entered: ", blood_pressure)
#------------Displaying Data----------------------
hyper = False 
if bp_Systolic >= 130 and bp_Diastolic >= 90:
    st.error(f"Warning: The your blood pressure values indicates that you have hypertension, please contact a medical professional for the best next steps!")
    hyper = True
else:
    st.write(f"Thank you for documenting your blood pressure with us today.")

if hyper == True and Protein_level in ["1+", "2+", "3+", "4+"]:
    st.error(f"Warning: the combination of your documented blood pressure and your protein levels indicate a high risk for pre-eclampsia, please contact a medical professional.")
    hyper = True
else:
    st.write(f"We appreciate you documenting your vitals today.")
#st.write("Current time: ", today)
st.write(nam, ", todays data is: ", weight, ",", Protein_level, ",", bp_Systolic , "/", bp_Diastolic)

#I need to append all the data to the csv file

styles = {
    'material-icons': {
        'color': 'red'
    },
    'text-icon-link-close-container': {
        'box-shadow': '#3896de 0px 4px'
    },
    'notification-text': {
        '': ''
    },
    'close-button': {
        '': ''
    },
    'link': {
        '': ''
    }
}

#custom_notification_box(
#    icon='info',
#    textDisplay='Please complete your form...',
#    externalLink='more info',
#    url='#',
#    styles=styles,
#    key="foo"
#)
#Basically I made a csv file of the patient data and I'm trying find a way to read from that csv file, then it would check if the patient in the csv file has been recording their results on time (X amount of hours), if they havent, then a pop up would appear saying that they need to record their results and then they would be able to do so.

#Info gathered should be sent over to a database that will
#"if needed" be sent over to the physician
#if time between last phlevel test and the current time is less
#4 hours, then send a notification to the patient

# Page 1: weight blood pressure
# Page 2: Data visual of blood pressure and weight
# Page 3: upload picture of urine sample , run
#If streamlit codes doesn't run, enter "streamlit run 1blood_weight.py" in the shell terminal

#Notification, interval

#Im also installing this plugin for Streamlit that allows for custom notification messaging

# USE "pip install streamlit-custom-notification-box" in the shell terminal
#pip install streamlit-pretty-notification-box

#https://www.youtube.com/watch?v=Mz12mlwzbVU

#24 hr bloo
#30 min blood