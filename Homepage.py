import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🧊",
    layout="wide",
)

st.title("Homepage")
st.sidebar.success("Welcome to the homepage!")

st.divider()

st.subheader("Introduction")


st.markdown(
    r"""
Welcome to the FitbitExecution app documentation! An app developed by the stress & psychopathology lab (Roee Admon, PI) to extract, analyze and visualize Fitbit data. This series of tutorials is designed to illustrate the use of the FitbitExecution app, step-by-step. The app itself is installed in a designated computer in our lab, where project managers can run it independently except for the initial setup, which will require assistance from our project maintainer. 


Generally, the code is meant to be executed sequentially where each step is dependent on the execution of the previous steps (with some exclusions). We suggest going over each step by using an example of one subject. 


After properly setting up a project and downloading subjects' data, each subject's data is preprocessed with some assumptions and informed choices we made based on our experience. Next, the user is expected to visually inspect each subject's output and approve it before proceeding to the next step. Then outputs are grouped into group-level outputs and visualized at the group level which should also be visually examined to detect any anomalies. The result is a series of .csv outputs which can be used for further analyses, with different resolutions (minute, daily or grand average). 


<h3> Final tips before diving into the code: </h3>

Make sure you fully understand the assumptions that are made in each step of analysis as described in this documentation.

<br> Always, but always, visually inspect your output! </br>

Take the time to go over your setup files before running the code. Validate formatting (e.g. dates are in DD/MM/YYYY format), that you have downloaded all the folders and that they matched to the Subjects Dates.csv file and that you went through your notes to detect any irregularities in data recording. Any irregular pattern can affect code running. 


<h3> Here is an overview of the different sections: </h3> 

1. First steps: create the project folder, create necessary files (subjects Dates, not in Israel) and raw data folder. 

2. Download API: connect subject's account to an API. Use it for automatically downloading raw data folders (recommended). <br> project maintainer help is required. </br>

3. Set up: create and validate “processed data” folder. This is the main working directory.  This directory contains relevant and format-unified raw data, outputs, and metadata. Registration to FitbitExecution app is done in this step. <br> project maintainer help is required. </br>

4. Extract Sleep Data: extract sleep data, which is used as a source for many features calculation. 

5. Preprocessing: raw data of heart rate and steps are down sampled into a 1-minute resolution, cleaned and converted into csv files. 

6. Combine step: sleep, step, and heart rate data are combined into one 1-minute resolution .csv file to be used for further analysis. Then, various features are calculated based on these files.  

7. Stats visualization visualizes the 1-minute resolution file. Important step to detect any abnormalities in the data. 

8. Time Series visualization: visualizes the time series of each signal collected from the data. Important step to detect any abnormalities in the data. 

9. EDA analysis: EDA measure is available on-demand in some FITBIT devices. His step extracts EDA measures from each subject. 

10. HRV analysis:   users that are subscribed to FITBIT premium can benefit from additional features such as sleep HRV and respiratory rate and daily device temperature. This step is for extraction data from these data sources. 

11. Final file: the result of all features available, this is the main file that is used for data analysis. 


    """, unsafe_allow_html=True
)
