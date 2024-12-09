import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import polars as pl


st.set_page_config(
    page_title="Final File",
    page_icon="🙌",
    layout="wide",
)

st.title("Final File Page")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this step the code will take all available data that we already run and will combine it into one final file that will be stored in the Experiment\Processed Data\ Outputs folder. When one wishes to use summary statistics for the entire measuring period, it is recommended to use this file. 


"""
)

st.divider()

with st.expander("1. How to extract the Final File for all subjects?"):


    dependencies_container = st.container(border=True)

    dependencies_container.markdown(
        """
        Before you run the Final File script, ensure that you have the following:
        - Sleep All Subjects csv file after the 'Extract Sleep Data' step.
        - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
        - Sleep Daily Summary Full Week csv files in the output folder after the 'Extract Sleep Data' step.
        - Full Week Summary of Heart Rate Metrics By Activity csv files in the output folder after the 'Combine Step' step.
        - * Summary of HRV Tempeture Respiratory at sleep files in the output folder after the 'HRV Analysis' step.
        - * EDA Summary files in the output folder after the 'EDA Analysis' step.

        * The files are not mandatory, but it is recommended to have them in the output folder for full output files if possible.
        """
    )


    st.markdown(
        """
    The 'Final File' page in our app is where we aggregate the processed data from the 'Extract Sleep Data', 'Combine Step', 'HRV Analysis', and 'EDA Analysis' steps for all subjects in the project.


    To extract the Final File for all subjects, follow these steps:

    1. Open the app.

    2. Click on the 'Final File' tab.

    3. Load your project by selecting the project and clicking on the 'Load' button.

    4. Wait for the app to load data table.

    5. Review the table to ensure that each subject has the necessary files, as described above.

    6. By selecting subjects from the table and click on the 'Show available data' button, you can see the content of the available data files for the selected subjects (here you can select more than one subject).

    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-19 174906.png"
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-19 175002.png"
    )


    st.markdown(
        """
    7. Filter the subjects by checking or unchecking the boxes of the 'run' column.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-19 175041.png"
    )

    st.markdown(
        """
    8. Click on the 'Run Final Processing' button to run the Final File script.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-19 175122.png"
    )

    st.markdown(
        """
    9. After the Final File generating process started, a black window will appear with the progress of the processing.

    10. After the processing is finished, the black window will close, and the Final file will be saved in the project output folder.
    """
    )

    st.divider()

with st.expander("2. How to review the extracted Final File?", icon="🚿"):
    st.markdown(
        """
        Not ready yet!
        """
    )

st.divider()

with st.expander('Show source code'):
    st.code(
        r"""
from flask import session
from dash import dcc, html, Dash, dependencies, dash_table, Input, Output, State, Patch, MATCH, ALL, callback
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import bioread as br
import h5py
import webview
# import dash_core_components as dcc
from flask import Flask
import subprocess
import platform
import base64
import io
from pymongo import MongoClient
import dash_ag_grid as dag
import dash
from datetime import datetime
from typing import Optional
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import configparser
import numpy as np
import polars as pl
import datetime
import logging
import pickle
import shutil
import json
import time
import sys
import os
import re
import tkinter as tk
from tkinter import filedialog
if os.path.exists(rf'C:\Users\PsyLab-6028'):
    sys.path.append(r'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages')
else:
    sys.path.append(r'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages')

import UTILS.utils as ut
# from Test.Remove_sub.utils import get_latest_file_by_term as new_get_latest_file_by_term
import warnings
warnings.filterwarnings('ignore')





def main(project, now, username):
    FIRST = 0
    LAST = -1
    if os.path.exists(rf'C:\Users\PsyLab-6028'):
        exeHistory_path = Path(r'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\ExecutionHis\exeHistory.parquet')
    else:
        exeHistory_path = Path(r'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\ExecutionHis\exeHistory.parquet')

    exeHistory = pl.read_parquet(exeHistory_path)
    if os.path.exists(rf'C:\Users\PsyLab-6028'):
        paths_json = json.load(open(r"C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\Pconfigs\paths.json", "r"))
    else:
        paths_json = json.load(open(r"C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\Pconfigs\paths.json", "r"))    

    
    project_path = Path(paths_json[project])



    DATA_PATH, OUTPUT_PATH, ARCHIVE_PATH, AGGREGATED_OUTPUT_PATH, METADATA_PATH, SUBJECT_FOLDER_FORMAT = ut.declare_project_global_variables(project_path)

    AGGREGATED_OUTPUT_PATH_HISTORY = ut.output_record(OUTPUT_PATH, 'Aggregated Output',username, now)

    if not AGGREGATED_OUTPUT_PATH_HISTORY.exists():
        os.makedirs(AGGREGATED_OUTPUT_PATH_HISTORY)
    if os.path.exists(rf'C:\Users\PsyLab-6028'):
        PROJECT_CONFIG = json.load(open(r'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\Pconfigs\paths data.json', 'r'))
    else:
        PROJECT_CONFIG = json.load(open(r'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\Pconfigs\paths data.json', 'r'))   

    SUBJECTS_DATES = METADATA_PATH.joinpath('Subjects Dates.csv')


    subjects_dates = pl.read_csv(SUBJECTS_DATES,
                                try_parse_dates=True)



    subjects_dates_df = subjects_dates.sort(by='Id').unique('Id').drop_nulls('Id')
    if os.path.exists(rf'C:\Users\PsyLab-6028'):
        selected_subjects_path = Path(rf'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\sub_selection\{project}_sub_selection_folders_EDA.parquet')
    else:
        selected_subjects_path = Path(rf'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\sub_selection\{project}_sub_selection_folders_EDA.parquet') 
        
    subjects_to_run_on = []

    if not selected_subjects_path.exists():
        print(f'Selected subjects file does not exist for {project}')
        time.sleep(10)
        quit()
    else:
        selected_subjects = pl.read_parquet(selected_subjects_path)
    
        subjects_to_run_on = selected_subjects['subject'].to_list()

    run_on_specific_subjects = True

    subjects_with_missing_stress_files = []
    subjects_with_weird_values = []
   
    # Create an empty list to hold any subjects that are missing any type of files
    subjects_with_missing_computed_temperature_files_files = []
    subjects_with_missing_json_files = []
    subjects_with_missing_respiratory_files = []
    subjects_with_missing_HRV_details_files = []
    subjects_with_missing_device_temperature_files = []
    print('Calculate Final All Subjects Aggregation')
    # Get latest file of Sleep Daily Summary Full Week.csv
    sleep_daily_summary_full_week_file = ut.new_get_latest_file_by_term('Sleep Daily Summary Full Week', root=AGGREGATED_OUTPUT_PATH)
    # Read the file to a DataFrame
    sleep_daily_summary_full_week_df = pd.read_csv(sleep_daily_summary_full_week_file)

    # Get latest file of Full Week Summary of Heart Rate Metrics By Activity.csv
    full_week_heart_rate_of_sleep_summary_means_file = ut.new_get_latest_file_by_term('Full Week Summary of Heart Rate Metrics By Activity', root=AGGREGATED_OUTPUT_PATH)
    # Read the file to a DataFrame
    full_week_heart_rate_of_sleep_summary_means_df = pd.read_csv(full_week_heart_rate_of_sleep_summary_means_file)
    # Merge the two DataFrames
    full_week_summary_means_df = pd.merge(sleep_daily_summary_full_week_df, full_week_heart_rate_of_sleep_summary_means_df, on='Id',how='outer')

    # Get latest file of Summary Of HRV Temperature Respiratory At Sleep.csv
    HRV_tempe_resp_summary_file = ut.new_get_latest_file_by_term('Summary Of HRV Temperature Respiratory At Sleep', root=AGGREGATED_OUTPUT_PATH)

    # Validate that the DataFrame is not empty
    if not HRV_tempe_resp_summary_file.exists():
        print('No Summary Of HRV Temperature Respiratory At Sleep.csv files were found in the subjects folders')
        HRV_tempe_resp_summary_df = pd.DataFrame(columns=['Id']) # for not getting error in the merge
    else:
        # Read the file to a DataFrame
        HRV_tempe_resp_summary_df = pd.read_csv(HRV_tempe_resp_summary_file)
    # Merge the two DataFrames
    full_week_summary_means_df = pd.merge(full_week_summary_means_df, HRV_tempe_resp_summary_df, on='Id', how='outer')

    # Get latest file of Mindfulness Summary.csv
    mindfulness_summary_file = ut.new_get_latest_file_by_term('EDA Summary', root=AGGREGATED_OUTPUT_PATH)

    # Validate that the DataFrame is not empty
    if not mindfulness_summary_file.exists():
        print('No EDA Summary.csv files were found in the subjects folders')
        mindfulness_summary_df = pd.DataFrame(columns=['Id']) # for not getting error in the merge
    else:
        # Read the file to a DataFrame
        mindfulness_summary_df = pd.read_csv(mindfulness_summary_file)

    # Merge the two DataFrames
    full_week_summary_means_df = pd.merge(full_week_summary_means_df, mindfulness_summary_df, on='Id',how='outer')


    # check if Final All Subjects Aggregation.csv exists in the aggregated output folder
    if not os.path.exists(AGGREGATED_OUTPUT_PATH.joinpath('Final All Subjects Aggregation.csv')):
        last_final_aggregation_df = pd.DataFrame(columns=full_week_summary_means_df.columns)
    else:
        # Get the last final aggregation file
        last_final_aggregation_file = ut.new_get_latest_file_by_term('Final All Subjects Aggregation', root=AGGREGATED_OUTPUT_PATH)
    
        # Read the file to a DataFrame
        last_final_aggregation_df = pd.read_csv(last_final_aggregation_file)
    
    # Replace the updated rows by subject id
    last_final_aggregation_df = last_final_aggregation_df.set_index('Id')
    full_week_summary_means_df = full_week_summary_means_df.set_index('Id')
    print('Update the Final All Subjects Aggregation file')
    tqdm_subjects = tqdm(full_week_summary_means_df.index)
    # If the subject is not in the last final aggregation file, add it to the file
    for subject in tqdm_subjects:
        tqdm_subjects.set_description(f'Subject {subject}')
        # Check if the subject is not in last_final_aggregation_df
        if subject not in last_final_aggregation_df.index:
            # If not, append the row corresponding to the subject from full_week_summary_means_df to last_final_aggregation_df
            new_row = full_week_summary_means_df.loc[subject]
            # Ensure new_row is a DataFrame for append to work correctly
            if isinstance(new_row, pd.Series):
                new_row = new_row.to_frame().T
            last_final_aggregation_df = pd.concat([last_final_aggregation_df, new_row])
        else:
            # If the subject is already in the DataFrame, update its row
            if run_on_specific_subjects and subject not in subjects_to_run_on:
                continue
            
            last_final_aggregation_df.loc[subject] = full_week_summary_means_df.loc[subject]

    # Ensure the index is still unique and correct after the operation
    last_final_aggregation_df = last_final_aggregation_df[~last_final_aggregation_df.index.duplicated(keep='last')]
            
    # Reset the index
    last_final_aggregation_df = last_final_aggregation_df.reset_index()

    last_final_aggregation_df = last_final_aggregation_df.rename(columns={'index': 'Id'})

    # Sort by Id column
    last_final_aggregation_df = last_final_aggregation_df.sort_values(by=['Id'])
    
    # drop nan columns
    last_final_aggregation_df = last_final_aggregation_df.dropna(axis=1, how='all')


    # Save the updated file to the project aggregated output folder
    last_final_aggregation_df.to_csv(AGGREGATED_OUTPUT_PATH_HISTORY.joinpath(f'Final All Subjects Aggregation.csv'), index=False)
    
    ut.check_for_duplications(AGGREGATED_OUTPUT_PATH, AGGREGATED_OUTPUT_PATH_HISTORY)

    





# Function to get the last Friday of March and last Sunday of October for a given year
def get_dst_change_dates(year):
    # Last Friday of March
    last_day_march = datetime.datetime(year, 3, 31)
    last_friday_march = last_day_march - datetime.timedelta(days=(last_day_march.weekday() + 3) % 7)

    # Last Sunday of October
    last_day_october = datetime.datetime(year, 10, 31)
    last_sunday_october = last_day_october - datetime.timedelta(days=(last_day_october.weekday() + 1) % 7)

    return last_friday_march, last_sunday_october

# Function to check if a date is a DST change date
def is_dst_change(date):
    year = date.year
    last_friday_march, last_sunday_october = get_dst_change_dates(year)
    return date.date() == last_friday_march.date() or date.date() == last_sunday_october.date()


                    


                    


            

            



            
    # except Exception as e:
    #     print(e)
    #     time.sleep(10)



def concate_to_old(term, path, new_df):
    old_path = ut.new_get_latest_file_by_term(term, root=path)
    if new_df.empty:
        if not old_path.exists():
            return pd.DataFrame()
        
        return pd.read_csv(old_path)
    if old_path.exists():
        old_df = pd.read_csv(old_path)
        
        for subject in new_df['Id'].unique():
            if subject in old_df['Id'].unique():
                old_df = old_df[old_df['Id'] != subject]
        new_df = pd.concat([old_df, new_df])
        new_df = new_df.sort_values(by=['Id'])
        return new_df
    else:
        return new_df

def valid_sleep(subject_sleep_df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function gets a DataFrame with sleep data of a subject and returns a DataFrame column with the valid sleep data.
    Valid sleep data is defined as:
                1. Between 20:00 to 08:00
                2. More than 3 hours of sleep
                3. If there are multiple sleep at night, the function will set True for the longest sleep and False for the rest.
    # the column names that the dataframe must have are:
    SleepStartTime
    DateOfSleepEvening
    If there are multiple sleep at night, the function will set True for the longest sleep and False for the rest.
    It does it by group by date and select the longest sleep at night.
    :param subject_sleep_df: DataFrame with sleep data of a subject
    :return: DataFrame column with the valid sleep column (boolean column)

    '''
    # Create a copy of the original DataFrame within the function and modify the copy.
    subject_sleep_df_copy = subject_sleep_df.copy()
    # Create a boolean mask to identify rows with valid sleep times based on the hour between 20:00 in the evening to 08:00 at the morning.
    mask_valid_rows_by_hour = (subject_sleep_df_copy['SleepStartTime'].dt.hour < 8) | (subject_sleep_df_copy['SleepStartTime'].dt.hour >= 20)
    # Add a new column to the DataFrame indicating whether each row has valid sleep times
    subject_sleep_df_copy['ValidSleep'] = mask_valid_rows_by_hour
    valid_subject_sleep_df_copy = subject_sleep_df_copy.loc[subject_sleep_df_copy['ValidSleep'] == True]
    # group by DateOfSleepEvening and iterate over each group
    for date, group in valid_subject_sleep_df_copy.groupby('DateOfSleepEvening'):
        max_index = group['SleepTimeInMinutes (our Calculation: SleepEndTime-SleepStartTime)'].idxmax()
        # Set False for all rows in the group
        for idx in group.index:
            subject_sleep_df_copy.at[idx, 'ValidSleep'] = False
        # Set True for the row with the longest sleep duration
        subject_sleep_df_copy.at[max_index, 'ValidSleep'] = True
    # Validate that each valid sleep has more than 3 hours of sleep, if not set False in ValidSleep column
    subject_sleep_df_copy.loc[
        (subject_sleep_df_copy['ValidSleep'] == True) & (subject_sleep_df_copy['SleepTimeInMinutes (our Calculation: SleepEndTime-SleepStartTime)'] <= 180),'ValidSleep'] = False

    return subject_sleep_df_copy['ValidSleep']


if __name__ == '__main__':
    
    try:
        param = sys.argv[1]
        now = sys.argv[2]
        user_name = sys.argv[3]

    except IndexError:
        param = 'FIBRO_TESTS'
        now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        user_name = 'Unknown'

    main(param, now, user_name)
"""
, language='python'
, line_numbers=True)
    

with st.expander('Example Final All Subjects Aggregation File'):
    spreadsheet(r"pages/assets/Final All Subjects Aggregation.csv")

st.divider()

st.subheader("Final file features dictionary")

st.markdown(
    """
Here you can search for a specific features (i.e. columns) that you can find in the related files.
"""
)


features_df = (
    pl.read_csv(r"pages/assets/features_dict.csv", encoding="ISO-8859-1")

)

# create a session state to store the results dataframe
if "result_df" not in st.session_state:
    st.session_state.result_df = None

with st.form("search"):
    st.write("Search for a feature")
    text_input = st.text_input("Feature or file name").lower()
    type_of = st.radio(
        "Search by 👉",
        key="visibility",
        options=["Feature name", "File name", "Both" , "Description"],
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")


    show_results = False

    if submitted:
        if type_of == "Feature name":
            result_df = (
                features_df
                .filter(
                    pl.col("Feature").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )
        elif type_of == "File name":
            result_df = (
                features_df
                .filter(
                    pl.col("File").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )

        elif type_of == "Both":
            result_df = (
                features_df
                .filter(
                    pl.col("Feature").str.to_lowercase().str.contains(text_input, strict=False)
                    | pl.col("File").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )
        elif type_of == "Description":
            result_df = (
                features_df
                .filter(
                    pl.col("Description").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )

        
        
        st.session_state.result_df = result_df

        st.write("Results for ", text_input, type_of, " There is ", len(result_df), " results")

        show_results = True



if show_results:

    result_df = st.session_state.result_df

    # st.dataframe(result_df)

    for i in range(len(result_df)):
        with st.container(border=True):
            st.subheader(f"Feature: {result_df["Feature"][i]}")
            st.write(f"File: {result_df["File"][i]}")
            if result_df["Type"][i] == None:
                results_type = " "
            else:
                results_type = result_df["Type"][i]
            st.write(f"Type: {results_type}")
            st.write(result_df["Description"][i])
            st.divider()

            
            how= result_df["Proccess"][i]


            if how == None:
                how = ["No information available"]
            elif r'/n' in how:
                how = how.split(r'/n') 
            else:
                how = [how]

            st.write("How we got it:")

            for j in range(len(how)):
                st.write(how[j])
                
            # if result_df["Source Code Lines"][i] != None:
            #     st.write("Source Code Line: ", result_df["Source Code Lines"][i])


with st.expander('features further explanation'):
    st.markdown(
        """
| Column                                   | Meaning                                                                                          | How Calculated                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Id                                       | Identifier of each subject                                                                      | Extracted from the 'Id' column, which represents the unique identifier of each subject present in the 'Sleep Daily Summary Full Week.csv', 'Full Week Summary of Heart Rate Metrics By Activity.csv', 'Summary Of HRV Temperature Respiratory At Sleep.csv', and 'EDA Summary.csv' files.                                     |
| Various Sleep Metrics                    | Metrics related to sleep patterns and quality over the measuring period                        | These metrics are obtained from the 'Sleep Daily Summary Full Week.csv' file, which provides various sleep-related metrics for each subject over the entire week. They include parameters like 'Total Sleep Time (min)', 'Total Bed Time (min)', 'Total Awake Time (min)', and 'Total Time in Bed (min)'.                     |
| Various Heart Rate and Steps Metrics     | Metrics related to heart rate during different activities over the measuring period            | These metrics are obtained from the 'Full Week Summary of Heart Rate Metrics By Activity.csv' file, which contains heart rate-related metrics for each subject during different activities over the entire week. It includes parameters like 'Average Heart Rate during Sleep (bpm)', 'Average Heart Rate during Exercise (bpm)'. |
| Various HRV (Heart Rate Variability) Metrics | Metrics related to HRV, temperature, and respiratory during sleep                               | These metrics are obtained from the 'Summary Of HRV Temperature Respiratory At Sleep.csv' file, which provides HRV-related metrics for each subject during sleep. The metrics include 'HRV_RMSSD_mean', 'HRV_RMSSD_std', 'HRV_Coverage_mean', 'HRV_Coverage_std', 'HRV_Low_Frequency_mean', 'HRV_Low_Frequency_std', 'HRV_High_Frequency_mean', 'HRV_High_Frequency_std', 'Skin_Temperature_mean', 'Skin_Temperature_std', 'Skin_Temperature_min', 'Skin_Temperature_max', 'Sleep_Breaths_In_Minute_mean', and 'Sleep_Breaths_In_Minute_std'. |
| Various EDA (Electrodermal Activity) Metrics | Metrics related to EDA during mindfulness sessions                                             | These metrics are obtained from the 'EDA Summary.csv' file, which provides EDA-related metrics for each subject during mindfulness sessions. The metrics include 'mean_2_minutes_EDA_mindfulness', 'std_2_minutes_EDA_mindfulness', 'mean_valid_2_minutes_EDA_mindfulness', and 'std_valid_2_minutes_EDA_mindfulness'.            |

        """, unsafe_allow_html=True
    )