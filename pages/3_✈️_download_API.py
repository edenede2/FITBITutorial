import streamlit as st

st.set_page_config(
    page_title="Download API",
    page_icon="📦",
    layout="wide",
)

st.title("Download fitbit data from API")

st.divider()

st.write(
    """
It is possible to automatically download your data through the API. This is a platform provided by Fitbit\Google that allows researchers and APP developers to extract data from users. This is done once per account. 

    """
)

st.divider()

with st.expander("1. Get your Fitbit API token"):

    st.write(
        """
        To begin, you will need to log into your subject account (Google and fitbit emails are the same for this step) a fitbit developer account.

        This will allow you to register your application and get the necessary credentials to access the fitbit API for your subject account.
        
        Follow the steps below to set up your fitbit developer account.
        """
    )


    st.markdown(
        """
        :red[Important: The token is valid for 1 year. If you need to download the data again, you will need to repeat this process.]
        """
    )


    st.subheader("Instructions")




    st.write(
        """
        1. Open a text file on your computer by right-clicking on your desktop and selecting 'New' -> 'Text Document'.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 204755.png"
    )

    st.write(
        """
        2. Add the following titles to the text file:

            - subjects client Ids: Your OAuth 2.0 Client ID, we will get this ids from the fitbit developer website in the next steps.
            - url: The url to get the token, we will get this url from the fitbit developer website in the next steps.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210137.png"
    )

    st.write(
        """
        3. Save the text file in your 'Processed Data' 'Metadata' folder with the following name: 'api_tokens.txt'. We will use this file to store your fitbit API credentials.
        4. Go to the [fitbit developer website](https://dev.fitbit.com/) and open the 'Register an App' page.

        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 203716.png"
    )

    st.write(
        """
        4. Log in with your fitbit account credentials.
        
            """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 190824.png"
    )


    st.write(
        """
        5. Select the 'REGISTER AN APP' tab.
            
                """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 203851.png"
    )


    st.write(
        """
        6. Fill the form with the following information:

            - Application Name: Your subject name (should not include the word fitbit and should include 12 characters or less).
            - Description: A brief description of your application (should not include the word fitbit and should include more then 20 characters).
            - Application Website URL: https://www.google.com.
            - Organization: University of Haifa.
            - Organization Website URL: https://www.google.com.
            - Terms of Service URL: https://www.google.com.
            - Privacy Policy URL: https://www.google.com.
            - OAuth 2.0 Application Type: Personal.
            - Redirect URLs: http://localhost
            - Default Access Type: Read-Only.
            - OAuth 2.0 Client ID: Your OAuth 2.0 Client ID.
            
            After filling the form, accept the terms and conditions and click on the 'Register' button.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 204431.png"
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 204452.png"
    )

    st.write(
        """
        7. After registering your app, you will be redirected to the 'Manage My Apps' page. :red[DON'T CLOSE THIS PAGE]
        8. Open the 'api_tokens.txt' file that you created in step 2, write your subject id and copy the address below under the 'url' field.

            - https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23PTDL&redirect_uri=http://localhost&scope=activity%20heartrate%20location%20nutrition%20oxygen_saturation%20profile%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight&expires_in=31536000

        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210356.png"
    )

    st.write(
        """
        9. Copy the OAuth 2.0 Client ID that you received after registering your app and paste it in the 'api_tokens.txt' file under the 'subjects client Ids' field.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210317.png"
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210356.png"
    )


    st.write(
        """
        10. Modify the url by replacing the 'client_id' value with your OAuth 2.0 Client ID. Make sure to copy it correctly.
        11. Save the 'api_tokens.txt' file.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 213543.png"
    )

    st.write(
        """
        12. Go back to the fitbit developer website and make sure you are still logged in.
        13. Copy the url from the 'api_tokens.txt' file and paste it in the browser's address bar and press 'Enter'.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210653.png"
    )

    st.write(
        """
        14. You will be redirected to the verification page. 
        15. Make sure that the access for the requested data is allowed for a 1 year. If not make sure that the number of seconds is 31536000 in the end of your url.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210913.png"
    )


    st.write(
        """
        16. Select 'Allow All' and click on the 'Allow' button.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 210936.png"
    )


    st.write(
        """
        17. You will be redirected to the 'localhost' page. :red[Ignore the page content]
        18. Copy the address from the browser's address bar to the 'api_tokens.txt' file under the 'redirect_uri' field.
        """

    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211126.png"
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211204.png"
    )

    st.write(
        """
        19. Save the 'api_tokens.txt' file.
        20. Write a new title in the text file (if you don't have one) called 'access_token' and copy the access token from the redirect uri that you copied in the previous step. It should start after the 'access_token=' and end before the '&scope='.

        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211441.png"
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211604.png"
    )

    st.write(
        """
        21. Save the 'api_tokens.txt' file.
        22. We will use the tokens in the next step to download your fitbit data.
        """
    )


st.divider()

with st.expander("2. Download your fitbit data"):




    st.write(
        """
        In this step, we will guide you through the process of downloading your fitbit data from the fitbit API.
        """
    )

    st.subheader("Instructions")



    dependencies_container = st.container(border=True)

    dependencies_container.markdown(
        """
        Before you run the download api script, ensure that you have the following:
        - The 'Experiment' folder with the necessary structure.
        - The 'Data' folder in the 'Experiment' folder (can be empty)
        - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
        """
    )

    st.write(
        """
        1. Open the app.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 200217.png"
    )

    st.write(
        """
        2. Click on the 'download api' tab.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211742.png"
    )

    st.write(
        """
        3. Load your project by selecting the project and clicking on the 'Load' button.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 211820.png"
    )

    st.write(
        """
        4. Review the table with the subjects that just loaded. This table shows the content of the 'subjects dates.csv' file that we created in the previous steps.
        5. Open the 'api_tokens.txt' file and copy the 'access_token' value to the 'token' field in the table.

        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 212109.png"
    )


    st.write(
        """
        6. Select the subjects that you want to download the data for.
        7. Click on the 'Generate .zip file for selected subjects' button.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 212227.png"
    )


    st.write(
        """
        8. A black box will appear at the center of the screen. This box shows the progress of the download process.
        9. Wait until the download is complete, the box will disappear when the download is done.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 214117.png"
    )

    st.write(
        """
        10. You can find the downloaded zip files in the 'Data' folder in the 'Experiment' folder of your project.
        11. Open the Data folder and right-click on the zip file that you just downloaded and select 'Extract here'.
        12. Go to the 'set up' tab to continue with the next steps.
        """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 212657.png"
    )

st.divider()

with st.expander('Show source code'):
    st.code(
        r"""
import requests
import pickle
from pathlib import Path
import shutil
import pandas as pd
import numpy as np
import plotly.express as px
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import datetime
import time as ti
from datetime import datetime, timedelta, time
from datetime import date as dt
import json
import zipfile
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED
import os
import sys
import polars as pl
sys.path.append(r'G:\Shared drives\AdmonPsy - Code\Idanko\Scripts')

import UTILS.utils as ut




global FILES_DICT

FILES_DICT = {'csv': [], 'json': []}


# Function to combine time with the date and reformat
def merge_date_and_time(given_date, time_str):
    # Combine given date and time string
    combined_str = f"{given_date} {time_str}"
    # Convert to datetime object
    dt = datetime.strptime(combined_str, "%Y-%m-%d %H:%M:%S")
    # Reformat to desired format
    return dt.strftime("%m/%d/%y %H:%M:%S")

def getTempFiles(path, start_date, end_date, token):
    print(f'Starting to download temperature data')

    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')
    SleepPath = Path(path).joinpath('Sleep')
    if not SleepPath.exists():
        SleepPath.mkdir()

    responses = []

    date_ranges_dict = {}

    if len(date_range) >= 30:
        if len(date_range) >= 60:
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[60]
            date_range_2 = [start_date_1, end_date_1]

            start_date_2 = date_range[61]
            end_date_2 = date_range[-1]
            date_range_3 = [start_date_2, end_date_2]

            date_ranges_dict = {1: date_range_1, 2: date_range_2, 3: date_range_3}

        else:
            # Generate start and end dates that have a maximum of 30 days between them
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[-1]
            date_range_2 = [start_date_1, end_date_1]

            date_ranges_dict = {1: date_range_1, 2: date_range_2}
    else:
        start_date = date_range[0]
        end_date = date_range[-1]
        date_ranges_dict = {1: [start_date, end_date]}

    for key, date_range in date_ranges_dict.items():
        
        start_date = date_range[0].strftime('%Y-%m-%d')
        end_date = date_range[1].strftime('%Y-%m-%d')
        print(f'Start date: {start_date}, End date: {end_date}')
        url = f'https://api.fitbit.com/1/user/-/temp/skin/date/{start_date}/{end_date}.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        responses.append(response)

        if response.status_code == 200:
            response = response.json()
            # create a csv file with the data
            for item in response['tempSkin']:
                timestamp = f"{item['dateTime']} 00:00"
                dailyTempDF = pd.DataFrame({'recorded_time': [timestamp] , 'temperature': [item['value']['nightlyRelative']], 'sensor_type': 'UNKNOWN'}, index=[0])
                dailyTempDF.to_csv(SleepPath.joinpath('Device Temperature - ' + item['dateTime'] + ' API.csv'), index=False)
                with open(SleepPath.joinpath('Device Temperature - ' + item['dateTime'] + ' API.csv'), 'w') as newFTemp:
                    FILES_DICT['csv'].append(newFTemp)
        else:
            print(f'Error {response.status_code}: {response.text}')
            print(f'While downloading temperature data for {start_date} to {end_date}')
            print(f'Reason: {response.reason}')
        print(f'Finished downloading temperature data')


    return responses

def getHRVfiles(path, start_date, end_date, token):
    print(f'Starting to download Heart Rate Variability data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')

    completed_dates = []

    SleepPath = Path(path).joinpath('Sleep')
    if not SleepPath.exists():
        SleepPath.mkdir()

    responses = []

    for date in date_range:
        print(f'Downloading HRV data for {date}')
        newDfHRV = pd.DataFrame({'timestamp': [], 'rmssd': [], 'coverage': [], 'high_frequency': [], 'low_frequency': []})

        date = date.strftime('%Y-%m-%d')
        url = f'https://api.fitbit.com/1/user/-/hrv/date/{date}/all.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        responses.append(response)

        if response.status_code == 200:
            response = response.json()
            # create a csv file with the data
            for item in response['hrv']:
                date = item['dateTime']
                for minute in item['minutes']:
                    timestamp = minute['minute'].replace('T', ' ')
                    timestamp = pd.to_datetime(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    rmssd = minute['value']['rmssd']
                    coverage = minute['value']['coverage']
                    highFrequency = minute['value']['hf']
                    lowFrequency = minute['value']['lf']
                    new_row = pd.DataFrame({'timestamp': [timestamp], 'rmssd': [rmssd], 'coverage': [coverage], 'high_frequency': [highFrequency], 'low_frequency': [lowFrequency]})
                    newDfHRV = pd.concat([newDfHRV, new_row], ignore_index=True)
            print(f'Finished downloading HRV data for {date}')
            completed_dates.append(date)

        else:
            print(f'Error {response.status_code}: {response.text}')
            print(f'While downloading HRV data for {date}')
            print(f'Reason: {response.reason}')

        newDfHRV.to_csv(SleepPath.joinpath('Heart Rate Variability Details - ' + date + '.csv'), index=False)
        with open(SleepPath.joinpath('Heart Rate Variability Details - ' + date + '.csv'), 'w') as newFHRV:
            FILES_DICT['csv'].append(newFHRV)
            

    print(f'Finished downloading HRV data')
    print(f'Completed dates: {completed_dates}')
    return responses




def getfilesHR(path, start_date, end_date, token):
    print(f'Starting to download heart rate data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')
    responses = []

    completed_dates = []

    PhysicalActivityPath = Path(path).joinpath('Physical Activity')
    if not PhysicalActivityPath.exists():
        PhysicalActivityPath.mkdir()

    for date in date_range:
        print(f'Downloading heart rate data for {date}')
        date = date.strftime('%Y-%m-%d')
        url = f'https://api.fitbit.com/1.2/user/-/activities/heart/date/{date}/1d/1sec/time/00:00/23:59.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()
            responses.append(response)

            # open the json file
            if 'Request failed with status code 502' in response:
                print(f'Error 502: Bad Gateway - {date} from {path}')
                continue
            # take the date from the json file
            date = response['activities-heart'][0]['dateTime']
            # create a new file
            newFile = 'api-heart_rate-' + date + '.json'
            # write the data to the new file [{"dateTime": "${date} ${data.activities-heart-intraday.dataset.time}", "value": {"bpm": ${data.activities-heart-intraday.dataset.value}, "confidence": 2}}]
            with open(PhysicalActivityPath.joinpath(newFile), 'w') as newFHR:
                # newFHR.write('[{\n')
                for item in response['activities-heart-intraday']['dataset']:
                    item['dateTime'] = merge_date_and_time(date, item['time'])
                    # newFHR.write('"dateTime": "' + date + ' ' + item['time'] + '", "value": {"bpm": ' + str(
                    #     item['value']) + ', "confidence": 2}\n')
                    # newFHR.write('},{\n')
                    item['value'] = {'bpm': item['value'], 'confidence': 2}                
                
                newFHR.write(json.dumps(response['activities-heart-intraday']['dataset'], indent=4))
                FILES_DICT['json'].append(newFHR)
        else:
            print(f'Error {response.status_code}: {response.text}')
            print(f'While downloading heart rate data for {date}')
            print(f'Reason: {response.reason}')

        print(f'Finished downloading heart rate data for {date}')
        completed_dates.append(date)

    print(f'Finished downloading heart rate data')
    print(f'Completed dates: {completed_dates}')
    return responses

def getfilesSteps(path, start_date, end_date, token):
    print(f'Starting to download steps data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')
    completed_dates = []
    steps_df = pd.DataFrame(columns=['timestamp', 'steps'])

    responses = []

    PhysicalActivityPath = Path(path).joinpath('Physical Activity')
    if not PhysicalActivityPath.exists():
        PhysicalActivityPath.mkdir()

    for date in date_range:
        date = date.strftime('%Y-%m-%d')
        url = f'https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d/1min/time/00:00/23:59.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()
            responses.append(response)

            # open the json file
            if 'Request failed with status code 502' in response:
                continue
            # take the date from the json file
            date = response['activities-steps'][0]['dateTime']
            # create a new file
            newFile = 'api-steps-' + date + '.json'
            # write the data to the new file [{"dateTime": "${date} ${data.activities-heart-intraday.dataset.time}", "value": {"bpm": ${data.activities-heart-intraday.dataset.value}, "confidence": 2}}]
            
            
            for item in response['activities-steps-intraday']['dataset']:
                item['dateTime'] = merge_date_and_time(date, item['time'])

                # newF.write('"dateTime": "' + date + ' ' + item['time'] + '", "value": ' + str(item['value']))
                # newF.write('\n},{\n')

                new_row = pd.DataFrame({'timestamp': [date + ' ' + item['time']], 'steps': [item['value']]})
                steps_df = pd.concat([steps_df, new_row], ignore_index=True)
            # newF.write(json.dumps(response['activities-steps-intraday']['dataset'], indent=4))
            FILES_DICT['json'].append(response['activities-steps-intraday']['dataset'])
            completed_dates.append(date)
        else:
            print(f'Error {response.status_code}: {response.text}')
            print(f'While downloading steps data for {date}')
            print(f'Reason: {response.reason}')

    steps_df.to_csv(PhysicalActivityPath.joinpath('steps.csv'), index=False)
    print(f'Finished downloading steps data')
    print(f'Completed dates: {completed_dates}')
    return responses


def generateRespiratoryRateCSV(path, start_date, end_date, token):
    print(f'Starting to download respiratory rate data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')

    responses = []

    SleepPath = Path(path).joinpath('Sleep')
    if not SleepPath.exists():
        SleepPath.mkdir()
    date_ranges_dict = {}

    if len(date_range) >= 30:
        if len(date_range) >= 60:
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[60]
            date_range_2 = [start_date_1, end_date_1]

            start_date_2 = date_range[61]
            end_date_2 = date_range[-1]
            date_range_3 = [start_date_2, end_date_2]

            date_ranges_dict = {1: date_range_1, 2: date_range_2, 3: date_range_3}

        else:
            # Generate start and end dates that have a maximum of 30 days between them
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[-1]
            date_range_2 = [start_date_1, end_date_1]

            date_ranges_dict = {1: date_range_1, 2: date_range_2}
    else:
        start_date = date_range[0]
        end_date = date_range[-1]
        date_ranges_dict = {1: [start_date, end_date]}

    for key, date_range in date_ranges_dict.items():
        start_date = date_range[0].strftime('%Y-%m-%d')
        end_date = date_range[1].strftime('%Y-%m-%d')
        url = f'https://api.fitbit.com/1/user/-/br/date/{start_date}/{end_date}/all.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()
            responses.append(response)

            # open the json file
            if 'Request failed with status code 502' in response:
                continue
            for item in response['br']:
                timestamp = f"{item['dateTime']} 0:00:00"
                dailyRespiratoryRateDF = pd.DataFrame({'timestamp': [timestamp] , 'daily_respiratory_rate': [item['value']['fullSleepSummary']['breathingRate']]}, index=[0])
                dailyRespiratoryRateDF.to_csv(SleepPath.joinpath('Daily Respiratory Rate Summary - ' + item['dateTime'] + '.csv'), index=False)
                with open(SleepPath.joinpath('Daily Respiratory Rate Summary - ' + item['dateTime'] + '.csv'), 'w') as newF:
                    FILES_DICT['csv'].append(newF)
        else:
            print(f'Error {response.status_code}: {response.text}')
            print(f'While downloading respiratory rate data for {start_date} to {end_date}')
            print(f'Reason: {response.reason}')
        
    print(f'Finished downloading respiratory rate data')
    return responses

def getCalories(path, start_date, end_date, token):
    print(f'Starting to download calories data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')
    responses = []

    calories_df = pd.DataFrame(columns=['timestamp', 'calories'])
    completed_dates = []

    PhysicalActivityPath = Path(path).joinpath('Physical Activity')
    if not PhysicalActivityPath.exists():
        PhysicalActivityPath.mkdir()

    for date in date_range:
        print(f'Downloading calories data for {date}')
        date = date.strftime('%Y-%m-%d')
        url = f'https://api.fitbit.com/1/user/-/activities/calories/date/{date}/1d/1min/time/00:00/23:59.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()
            responses.append(response)

            # open the json file
            if 'Request failed with status code 502' in response:
                continue
            # take the date from the json file
            date = response['activities-calories'][0]['dateTime']
            # create a new file
            newFile = 'calories-' + date + '.json'
            # write the data to the new file [{"dateTime": "${date} ${data.activities-heart-intraday.dataset.time}", "value": {"bpm": ${data.activities-heart-intraday.dataset.value}, "confidence": 2}}]
            with open(PhysicalActivityPath.joinpath(newFile), 'w') as newF:
                
                for item in response['activities-calories-intraday']['dataset']:
                    item['dateTime'] = merge_date_and_time(date, item['time'])

                    new_row = pd.DataFrame({'timestamp': [date + ' ' + item['time']], 'calories': [item['value']]})
                    calories_df = pd.concat([calories_df, new_row], ignore_index=True)
                newF.write(json.dumps(response['activities-calories-intraday']['dataset'], indent=4))
                FILES_DICT['json'].append(newF)
        print(f'Finished downloading calories data for {date}')
        completed_dates.append(date)

    print(f'Finished downloading calories data')
    print(f'Completed dates: {completed_dates}')
    calories_df.to_csv(PhysicalActivityPath.joinpath('calories.csv'), index=False)


def getSleepfiles(path, start_date, end_date, token):
    print(f'Starting to download sleep data')
    date_range = pd.date_range(start_date, end_date)
    print(f'Date range: {date_range}')

    responses = []

    SleepPath = Path(path).joinpath('Sleep')
    if not SleepPath.exists():
        SleepPath.mkdir()
    
    date_ranges_dict = {}

    if len(date_range) >= 30:
        if len(date_range) >= 60:
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[60]
            date_range_2 = [start_date_1, end_date_1]

            start_date_2 = date_range[61]
            end_date_2 = date_range[-1]
            date_range_3 = [start_date_2, end_date_2]

            date_ranges_dict = {1: date_range_1, 2: date_range_2, 3: date_range_3}

        else:
            # Generate start and end dates that have a maximum of 30 days between them
            start_date = date_range[0]
            end_date = date_range[30]
            date_range_1 = [start_date, end_date]

            start_date_1 = date_range[31]
            end_date_1 = date_range[-1]
            date_range_2 = [start_date_1, end_date_1]

            date_ranges_dict = {1: date_range_1, 2: date_range_2}
    else:
        start_date = date_range[0]
        end_date = date_range[-1]
        date_ranges_dict = {1: [start_date, end_date]}

    for key, date_range in date_ranges_dict.items():
        
        start_date = date_range[0].strftime('%Y-%m-%d')
        end_date = date_range[1].strftime('%Y-%m-%d')
        print(f'Start date: {start_date}, End date: {end_date}')
        url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{start_date}/{end_date}.json'
        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()['sleep']
            responses.append(response)

            # open the json file

            if 'Request failed with status code 502' in response:
                continue
            if '492' in response:
                print(response)
                continue
            # save the data to a json file
            response = json.dumps(response, indent=4)
            with open(SleepPath.joinpath('sleep-' + start_date + '.json'), 'w') as newF:
                newF.write(response)
                FILES_DICT['json'].append(newF)
    print(f'Finished downloading sleep data')
    return responses


def saveAsZIP(path, token, start_date, end_date,sub_name):
    print(f'Starting to download data for {sub_name}')
    with TemporaryDirectory() as temp_dir:
        print(f'Temporary directory created: {temp_dir}')


        temp_dir = Path(temp_dir)
        sub_temp_path = temp_dir.joinpath(sub_name)
        if not sub_temp_path.exists():
            sub_temp_path.mkdir()
            sub_temp_path.joinpath('FITBIT').mkdir()
        sub_temp_path = sub_temp_path.joinpath('FITBIT')
        sub_temp_path.joinpath('Sleep').mkdir()
        sub_temp_path.joinpath('Physical Activity').mkdir()
        sub_temp_path.joinpath('Stress').mkdir()
        print(f'Subject temporary directory created: {sub_temp_path}')
        sleep_responses_nova = getSleepfiles(sub_temp_path, start_date, end_date, token)
        steps_responses_nova = getfilesSteps(sub_temp_path, start_date, end_date, token)
        HR_responses_nova = getfilesHR(sub_temp_path, start_date, end_date, token)
        Respiratory_responses_nova = generateRespiratoryRateCSV(sub_temp_path, start_date, end_date, token)
        HRV_responses_nova = getHRVfiles(sub_temp_path, start_date, end_date, token)
        Temp_responses_nova = getTempFiles(sub_temp_path, start_date, end_date, token)
        Calories_responses_nova = getCalories(sub_temp_path, start_date, end_date, token)
        print(f'Finished downloading data for {sub_name}')

        print(f'Cleaning steps data for {sub_name}')
        clean_steps(sub_temp_path)
        # Create a ZipFile Object
        with ZipFile(path.joinpath(f'{sub_name}.zip'), 'w', compression=ZIP_DEFLATED) as zipObj:
            for folderName, subfolders, filenames in os.walk(temp_dir):
            
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, os.path.relpath(filePath, temp_dir))

        print(f'Zip file created for {sub_name}')
        print(f'Cleaning temporary directory for {sub_name}')
        shutil.rmtree(temp_dir)
        print(f'Temporary directory cleaned for {sub_name}')

        print(f'Extracting zip file for {sub_name}')
        with ZipFile(path.joinpath(f'{sub_name}.zip'), 'r') as zip_ref:
            zip_ref.extractall(path)
        print(f'Zip file extracted for {sub_name}')


def clean_steps(physical_activity_path):
    print('Cleaning steps data')
    # read the steps and calories dataframes that generated from the API
    steps_df = pd.read_csv(physical_activity_path.joinpath('Physical Activity').joinpath('steps.csv'))
    print(f'steps file found: {steps_df.head()}')
    steps_df['timestamp'] = pd.to_datetime(steps_df['timestamp'])
    # read the calories dataframe that generated from the API
    calories_df = pd.read_csv(physical_activity_path.joinpath('Physical Activity').joinpath('calories.csv'))
    print(f'calories file found: {calories_df.head()}')
    calories_df['timestamp'] = pd.to_datetime(calories_df['timestamp'])
    

    # merge the two dataframes on the timestamp column
    merged_df = pd.merge(steps_df, calories_df, on='timestamp', how='outer')
    print(f'merged file: {merged_df.head()}')
    # save the merged dataframe to a csv file
    merged_df.to_csv(physical_activity_path.joinpath('Physical Activity').joinpath('merged.csv'), index=False)
    print(f'merged file saved to {physical_activity_path.joinpath("Physical Activity").joinpath("merged.csv")}')
    min_calories_per_date = {}


    merged_df['date'] = merged_df['timestamp'].dt.date

    for date in merged_df['date'].unique():
        print(f'Getting min calories for {date}')
        min_calories_per_date[date] = merged_df[merged_df['date'] == date]['calories'].min()

    for index, row in merged_df.iterrows():
        date = row['date']
        if row['calories'] == min_calories_per_date[date] and row['steps'] == 0:
            merged_df.at[index, 'steps'] = np.nan
            merged_df.at[index, 'timestamp'] = np.nan



    # get new steps json file
    new_steps_df = pd.DataFrame(columns=['timestamp', 'steps'])
    # for index, row in merged_df.iterrows():
    #     new_row = pd.DataFrame({'timestamp': [row['timestamp']], 'steps': [row['steps']]})
    #     new_steps_df = pd.concat([new_steps_df, new_row], ignore_index=True)
    new_steps_df = merged_df[['timestamp', 'steps']]
    print(f'new steps file: {new_steps_df.head()}')


    # save the new steps json file
    new_steps = []
    for index, row in new_steps_df.iterrows():
        if pd.notna(row['timestamp']) and pd.notna(row['steps']):
            new_steps.append({
                "dateTime": row['timestamp'].strftime('%m/%d/%y %H:%M:%S'),
                "value": str(int(row['steps']))
            })
    print(f'new steps: {new_steps}')
    physical_activity_path = Path(physical_activity_path.joinpath('Physical Activity'))
    with open(physical_activity_path.joinpath(f'api-steps-{date}.json'), 'w') as newF:
        new_steps = json.dumps(new_steps, indent=4)
        newF.write(new_steps)
        FILES_DICT['json'].append(newF)
    print(f'new steps file saved to {physical_activity_path.joinpath("api_steps-2024-04-27.json")}')


def main(project, username, now):

    try:
        print('Downloading data...')
        try:
            exeHistory_path = Path(r'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\ExecutionHis\exeHistory.parquet')
        except Exception as e:
            exeHistory_path = Path(r'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\ExecutionHis\exeHistory.parquet')
        exeHistory = pl.read_parquet(exeHistory_path)

        try:
            paths_json = json.load(open(r'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\Pconfigs\paths data.json', 'r'))
        except:
            paths_json = json.load(open(r'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\Pconfigs\paths data.json', 'r'))

    
        project_path = Path(paths_json[project])



        # DATA_PATH, OUTPUT_PATH, ARCHIVE_PATH, AGGREGATED_OUTPUT_PATH, METADATA_PATH, SUBJECT_FOLDER_FORMAT = ut.declare_project_global_variables(project_path)

        # AGGREGATED_OUTPUT_PATH_HISTORY = ut.output_record(OUTPUT_PATH, 'Aggregated Output',username, now)

        # if not AGGREGATED_OUTPUT_PATH_HISTORY.exists():
        #     os.makedirs(AGGREGATED_OUTPUT_PATH_HISTORY)
        DATA_PATH = Path(project_path)
        if not DATA_PATH.exists():
            DATA_PATH.mkdir()


        try:
            api_data_path = Path(rf'C:\Users\PsyLab-6028\Desktop\FitbitDash\pages\sub_selection\{project}_sub_selection_download_api.parquet')
        except:
            api_data_path = Path(rf'C:\Users\PsyLab-7084\Documents\GitHub\FitbitDash\pages\sub_selection\{project}_sub_selection_download_api.parquet')
    
        data_df = pl.read_parquet(api_data_path)

        print('Folder created successfully')

        for sub in data_df.iter_rows():
            print(f'Downloading data for {sub[0]}')
            sub_name = sub[0]
            token = sub[5]
            start_date = pd.to_datetime(sub[1], format='%d/%m/%Y')
            end_date = pd.to_datetime(sub[3], format='%d/%m/%Y')
            path = Path(DATA_PATH)
            
            if not path.exists():
                path.mkdir()
            saveAsZIP(path, token, start_date, end_date, sub_name)
    except Exception as e:
        print(e)
        ti.sleep(15)
        



    # for sub in data_df.iter_rows():
    #     if not sub[0] in ['sub_011_T4','sub_012_T2', 'sub_012_T3','sub_012_T4', 'sub_015_T4','sub_016_T3', 'sub_016_T4', 'sub_017_T3']:
    #         continue
    #     sub_name = sub[0]
    #     token = sub[21]
    #     start_date = sub[22]
    #     end_date = sub[23]
    #     path = Path('/Users/edeneldar/JS learn/fitbitApiCall/data').joinpath(sub_name)
    #     if not path.exists():
    #         path.mkdir()
    #     saveAsZIP(path, token, start_date, end_date, sub_name)
        





if __name__ == '__main__':
    try:
        project = sys.argv[1]
        username = sys.argv[2]
        now = sys.argv[3]
        main(project, username, now)
    except Exception as e:
            project = 'MDMA'
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            username = 'PsyLab-6028'

            main(project, username, now)

        
        

    
""",
        language='python'
        , line_numbers= True   
    )