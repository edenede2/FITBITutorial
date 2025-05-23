import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import polars as pl



st.set_page_config(
    page_title="Preprocessing",
    page_icon="💓🚶‍♂️",
    layout="wide",
)


st.title("Steps & HR Data Preprocessing")


st.divider()

st.header("Introduction")

st.markdown(
    """
The 'preprocessing' step in our pipeline is where we clean, transform, and aggregate the heart rate and steps .json files that we have collected from the Fitbit watch in the 'set up' step. 

The overall goal is to convert the heart rate and .json files into a clean 1-minute resolution file. 

Basically, two csv files (one for heart rate and one for steps) are generated at the end of this step. These csv files are used only as an intermediate step that help merge and build the final 1-minute resolution file. In practice, we use the output of the ‘combine step’ tab which provides the final 1-minute resolution file and not the two files generated here. 

However, data cleaning is done in this step, so it is important to understand what are the cleaning criteria that are used.  

Some information on the raw .json files:

•	Each heart rate json file contains the heart rate data for a specific day.

•	Each steps json file contains the steps data for a specific month (starting from the 1st day of the month to the last day of the month).

•	The Heart Rate data is recorded in various resolutions (1-15 seconds) by the Fitbit watch. This means that each sample needs to be weighted according to the number of seconds it is based on (15 seconds sample should have larger weight compared to a 5 seconds sample). Sometimes the watch may not be able to collect the data due to various reasons. 

•	The Steps data is collected every 1 minute by the Fitbit watch. In the steps data, missing data due to (probably) storage limitations are common. Thus, steps data are expected to have more missing data compared to heart rate data. 

<br>**Heart rate preprocessing pipeline:**</br>

1.	Find all heart rate .json files in the range between the start and end of the measuring period (based in Subjects Dates.csv file). 

2.	Convert unequal samples into a 1-second vector of heart rate data. This is done using backward filling: Fills missing values with the value of the next sample that is not nan (allows weighting of samples).

3.	Omit invalid heart rate samples. valid heart rate data are defined as: 

    a. Confidence values should be above 0 (confidence is and indicator for sample validity ranging from 0-3 and provided by the Fitbit watch) 

    b. Heart rate bpm should be between 40 and 180 (can be modified by the user)

    c. Minutes should have 1 or more original heart rate samples, regardless of their length.

4.	Group bpm values by 1-minute to create a  1-minute resolution file. 

<br>**Steps preprocessing pipeline:**</br>

1.	Find all steps .json files 

2.	Convert .json files into a csv file 


:red[Note:] 

-	If downloading the data through the API (‘Download API’ tab), The steps jsons that we are downloading from the Fitbit API has no missing values and in the 'download api' step we are cleaning the json file to include the same values as the json files that we are downloading from the Fitbit website. To change it, try to involve the programmer to change the code in the Fitbit API to include the missing values in the steps json file.

-	The column ’Mode’ column in the heart rate.csv file is currently being ignored. 

""" , unsafe_allow_html=True
)

st.divider()



with st.expander("1. How do we run the 'preprocessing' step?"):



    dependencies_container = st.container(border=True)

    dependencies_container.markdown(
        """
        Before you run the preprocessing script, ensure that you have the following:
        - The 'Data' folder in the 'Processed Data' folder after running the 'set up' script.
        - The heart rate and the steps json files for all the subjects you want to extract the sleep data for in the 'Data' folder (after the set up step).
        - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
        """
    )

    st.markdown(
        """
    To run the 'preprocessing' step, follow the steps below:
    1. Open the app.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 200217.png"
    )

    st.markdown(
        """
    2. Click on the 'Preprocessing' tab.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 200217.png"
    )

    st.markdown(
        """
    3. Select your project from the dropdown menu and enter your name.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 154140.png"
    )

    st.markdown(
        """
    4. Click on the 'Load' button and wait for the table to load.
    5. Review the table, check for any missing hr or steps files, by clicking on specific subject and then on the 'Show available data' button.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 154441.png"
    )


    st.markdown(
        """
    6. Filter the run column by check or uncheck the box.
    7. When you are ready, click on the 'Run Preprocessing Step' button.
    """
    )


    st.image(
        r"pages/assets/Screenshot 2024-10-12 154722.png"
    )


    st.markdown(
        """
    8. After you click on the 'Run Preprocessing Step' button, a black window will appear with the progress of the preprocessing step.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 154801.png"
    )

    st.markdown(
        """
    9. When the preprocessing step is done, the black window will disappear.
    10. You can now see the outputs files in the 'Outputs' folder of your project.
    """
    )

st.divider()

with st.container(border=True):
    st.markdown(
    """
After the preprocessing step, we will have 4 csv files in sampling rate of 1 minute:

a.	sub_000_heartrate.csv: contains the heart rate data per minute.

b.	sub_000_steps.csv: contains the heart rate data per minute.

c.	steps.csv: (for all the subjects in the aggregated folder Experiment\Processed Data\aggregated outputs)

d.	steps.parquet:  (for all the subjects in the aggregated folder, this file is used to accelerate processing speed of the code, not for analysis)

    """)

st.divider()


with st.expander("Show source code"):
    st.code(
        r"""
        FIRST = 0
        LAST = -1
        exeHistory_path = Path(r'.\pages\ExecutionHis\exeHistory.parquet')   

        exeHistory = pl.read_parquet(exeHistory_path)
        paths_json = json.load(open(r".\pages\Pconfigs\paths.json", "r")) 


        project_path = Path(paths_json[project])



        DATA_PATH, OUTPUT_PATH, ARCHIVE_PATH, AGGREGATED_OUTPUT_PATH, METADATA_PATH, SUBJECT_FOLDER_FORMAT = ut.declare_project_global_variables(project_path)

        AGGREGATED_OUTPUT_PATH_HISTORY = ut.output_record(OUTPUT_PATH, 'Aggregated Output',username, now)

        if not AGGREGATED_OUTPUT_PATH_HISTORY.exists():
            os.makedirs(AGGREGATED_OUTPUT_PATH_HISTORY)
        
        PROJECT_CONFIG = json.load(open(r'.\pages\Pconfigs\paths data.json', 'r'))

        SUBJECTS_DATES = METADATA_PATH.joinpath('Subjects Dates.csv')

        try:
            subjects_dates = pl.read_csv(SUBJECTS_DATES,
                                        try_parse_dates=True)
        except:
            subjects_dates = pl.read_csv(SUBJECTS_DATES,
                                        parse_dates=True,
                                        encoding='utf-8')

        subjects_dates_df = subjects_dates.sort(by='Id').unique('Id').drop_nulls('Id')
        selected_subjects = pl.read_parquet(rf'.\pages\sub_selection\{project}_sub_selection_folders_Preprocessing.parquet')
            
    
        run_on_specific_subjects = True
        subjects_to_run_on = selected_subjects['subject'].to_list()

        subjects_with_missing_heart_rate_files = []
        print('Process Heart Rate Data')
        tqdm_subjects = tqdm(os.listdir(DATA_PATH))
        for subject in tqdm_subjects:
            if not re.search(r'\d{3}$', subject):
                continue
            if run_on_specific_subjects and subject not in subjects_to_run_on:
                continue
            tqdm_subjects.set_description(f'Subject: {subject}', refresh=True)
            # if the folder not look like 'sub_xxx' so skip it
            # if not re.fullmatch(SUBJECT_FOLDER_FORMAT, subject):
            #     continue #@TODO: GET BACK IN
            # Set up the path to the subject's sleep folder
            if not os.path.exists(OUTPUT_PATH.joinpath(subject)):
                os.mkdir(OUTPUT_PATH.joinpath(subject))
            heart_rate_json_directory = DATA_PATH.joinpath(f'{subject}\FITBIT\Physical Activity')
            try:
                # Read the subject_HR_json_data from the pickle file
                with open(OUTPUT_PATH.joinpath(subject).joinpath('from_code_subject_HR_df.pkl'), 'rb') as f:
                    subject_HR_df = pickle.load(f)
            except:
                # Find all "heart_rate-YYYY-MM-DD.json" files in the Physical Activity folder
                heart_rate_file_name_pattern = re.compile(r'^heart_rate-\d{4}-\d{2}-\d{2}.json')
                heart_rate_api_file_name_pattern = re.compile(r'^api-heart_rate-\d{4}-\d{2}-\d{2}.json')
                heart_rate_json_files = [file_name for file_name in os.listdir(heart_rate_json_directory)
                                        if heart_rate_file_name_pattern.search(file_name)]
                heart_rate_api_files = [file_name for file_name in os.listdir(heart_rate_json_directory)
                                        if heart_rate_api_file_name_pattern.search(file_name)]
                # If the subject is missing heart rate files, skip them and add their name to the list
                if not heart_rate_json_files:
                    if not heart_rate_api_files:
                        subjects_with_missing_heart_rate_files.append(subject)
                        continue  # skipping current subject
                if heart_rate_json_files:
                    # Sort heart rate files
                    heart_rate_json_files = sorted(heart_rate_json_files)
                    # Merge all heart rate files to one list
                    all_files_df = pl.DataFrame()
                    for json_hr_file in heart_rate_json_files:
                        file_df = pl.read_json(os.path.join(heart_rate_json_directory, json_hr_file))
                        all_files_df = pl.concat([all_files_df, file_df])

                    subject_HR_df = (
                        all_files_df
                        .with_columns(
                            pl.col('dateTime')
                            .str.strptime(pl.Datetime, '%m/%d/%y %H:%M:%S')
                            .dt.convert_time_zone('Israel')
                            .dt.replace_time_zone(None)
                            .dt.cast_time_unit('ns')
                        )  
                        .unnest('value')
                        .to_pandas()
                    )                

                    with open(OUTPUT_PATH.joinpath(subject).joinpath('from_code_subject_HR_df.pkl'), 'wb') as f:
                        pickle.dump(subject_HR_df, f)
                elif heart_rate_api_files:
                    # Sort heart rate files
                    heart_rate_api_files = sorted(heart_rate_api_files)
                    # Merge all heart rate files to one list
                    subject_HR_json_data = []
                    for file_name in heart_rate_api_files:
                        with open(heart_rate_json_directory.joinpath(file_name)) as f:
                            subject_HR_json_data.extend(json.load(f))

                    ########## Preprocess data ##########

                    # Convert to dataframe with the columns: 'dateTime', 'value', 'confidence'.
                    subject_HR_df = pd.json_normalize(subject_HR_json_data)  # TODO: small bottleneck
                    # Convert dates columns to datetime object: '2021-11-16T00:16:30.000' --> '2021-11-16 00:16:30'
                    subject_HR_df['dateTime'] = pd.to_datetime(subject_HR_df['dateTime'])  # TODO: big bottleneck

                    with open(OUTPUT_PATH.joinpath(subject).joinpath('from_code_subject_HR_df.pkl'), 'wb') as f:
                        pickle.dump(subject_HR_df, f)        
            # Rename columns
            if 'value.bpm' in subject_HR_df.columns:
                subject_HR_df = subject_HR_df.rename(columns={'value.bpm': 'bpm',
                                                            'value.confidence': 'confidence'})
                
            # Get start and end dates of experiment for current subject
            subject_dates = ut.get_subject_dates_of_experiment(subject, METADATA_PATH)
            try:
                # Mask valid rows. which are the dates that between the experiment start date and the experiment end date.
                subject_HR_df = subject_HR_df[
                    subject_HR_df['dateTime'].between(subject_dates.iloc[0]['ExperimentStartDateTime'],
                                                    subject_dates.iloc[0]['ExperimentEndDateTime'])]
                # if subject_dates['NotInIsrael'].values[0]:
                #     relevant_subject_steps_df_before = subject_HR_df[subject_HR_df['dateTime'] < subject_dates['NotInIsraelStartDate'].values[0]]
                #     relevant_subject_steps_df_after = subject_HR_df[subject_HR_df['dateTime'] > pd.to_datetime(subject_dates['NotInIsraelEndDate'].values[0]) + datetime.timedelta(days=1)]
                #     subject_HR_df = pd.concat([relevant_subject_steps_df_before, relevant_subject_steps_df_after])
                
                # if subject_dates['NotInIsrael_1'].values[0]:
                #     relevant_subject_steps_df_before = subject_HR_df[subject_HR_df['dateTime'] < subject_dates['NotInIsraelStartDate_1'].values[0]]
                #     relevant_subject_steps_df_after = subject_HR_df[subject_HR_df['dateTime'] > pd.to_datetime(subject_dates['NotInIsraelEndDate_1'].values[0]) + datetime.timedelta(days=1)]
                #     subject_HR_df = pd.concat([relevant_subject_steps_df_before, relevant_subject_steps_df_after])

            except:
                subjects_with_missing_heart_rate_files.append(subject)
                continue
            # # Remove all rows that are not valid
            # subject_HR_df = subject_HR_df[mask_valid_rows]

            ########## Create Dataframe 1: Select Valid data, resample the 'subject_HR_df' DataFrame by minute, backward-filling missing data ##########

            # Add a new column to the DataFrame named 'Valid'. Initialize it with 0 temporarily.
            subject_HR_df['valid'] = 0
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$old filter$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # Set 1 at 'Valid' column where confidence is above 1 and heart rate bpm is between 40 to 180.
            # subject_HR_df.loc[(subject_HR_df['confidence'] > 1) &
            #                            (subject_HR_df['bpm'] >= 40) &
            #                            (subject_HR_df['bpm'] <= 180), 'valid'] = 1
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$old filter$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            # Set 1 at 'Valid' column where confidence is above 1 and heart rate bpm is between 40 to 180.
            subject_HR_df.loc[(subject_HR_df['confidence'] >= con_threashold) &
                            (subject_HR_df['bpm'] >= min_hr_threashold) &
                            (subject_HR_df['bpm'] <= max_hr_threashold), 'valid'] = 1

            # Group by minute and count the number of bpm samples per minute.
            num_of_all_samples_df = subject_HR_df[['dateTime', 'bpm']].groupby(pd.Grouper(key='dateTime', freq='1Min')).agg(['count'])
            num_of_all_samples_df.columns = ['NumOfAllSamples']

            # if NumOfAllSamples is 0, set "unknown" value to Mode column
            num_of_all_samples_df.loc[num_of_all_samples_df['NumOfAllSamples'] == 0, 'Mode'] = 'unknown'
            # Select valid rows
            valid_heart_rate_merged = subject_HR_df.loc[subject_HR_df['valid'] == 1]
            # Group by minute and count the number of bpm samples per minute. Create data with one column named "bpm/count"
            num_of_valid_samples_df = valid_heart_rate_merged[['dateTime', 'bpm']].groupby(pd.Grouper(key='dateTime', freq='1Min')).agg(['count'])
            # Rename column "bpm/count" to "NumOfValidSamples"
            num_of_valid_samples_df.columns = ['NumOfValidSamples']

            # Add Mode column that equals to num_of_valid_samples_df
            num_of_valid_samples_df['Mode'] = num_of_all_samples_df['Mode']
            num_of_valid_samples_df['NumOfAllSamples'] = num_of_all_samples_df['NumOfAllSamples']
            ########## Create Dataframe 2: Resample the 'subject_HR_df' DataFrame by second, backward-filling missing data ##########

            # Set the index of subject_HR_df to dateTime. It is a must for upsampling by seconds.
            subject_HR_df = subject_HR_df.set_index('dateTime')
            # Resample 'subject_HR_df' DataFrame by second (without filter the valid rows), backward-filling missing data of the 4 (all) columns: 'dateTime', 'bpm', 'confidence', 'valid'.
            # Each row correspond to a second.
            # bfill(): Use next observation to fill the rows before / Fills missing values in the DataFrame with the value of the next row that is not nan.
            bpm_confidence_valid_resample_by_seconds = subject_HR_df.resample('S').bfill().reset_index()
            # Select rows from the DataFrame where the 'valid' column equals 1, and only keep the 'dateTime' and 'bpm' columns
            bpm_valid_resample_by_seconds_filtered = bpm_confidence_valid_resample_by_seconds.loc[bpm_confidence_valid_resample_by_seconds['valid'] == 1, ['dateTime', 'bpm']]
            # Group the filtered DataFrame by minute intervals on the 'dateTime' column and compute the mean and count of the 'bpm' column for each minute interval.
            # The count represents the number of seconds where the samples are valid (after up-sampling to minutes and backward fill) and also the number of valid samples after bfill.
            bpm_group_by_minute_after_bfill = bpm_valid_resample_by_seconds_filtered.groupby(pd.Grouper(key='dateTime', freq='1Min')).agg(['mean', 'count'])
            # Rename columns
            bpm_group_by_minute_after_bfill.columns = ['BpmMean', 'NumOfValidSamplesAfterBfill']

            ########## Merge Dataframe 1 ('BpmMean') and Dataframe 2 ('NumOfValidSamples', 'NumOfValidSamplesAfterBfill') by date ##########
            # creating dataframe with 3 columns: 'NumOfValidSamples', 'BpmMean', 'NumOfValidSamplesAfterBfill'.
            # 'outer': Use dateTime index from both dataframes. meaning if there is missing dateTime in one of them - it will appear with missing values.
            merged_heart_rate_df = num_of_valid_samples_df.merge(bpm_group_by_minute_after_bfill, how='outer', left_index=True, right_index=True)
            # Set nan in rows with less than 4 heart rate samples or in rows with less than 30 valid samples after bfill.
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$OLD FILTER$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # merged_heart_rate_df.loc[(merged_heart_rate_df['NumOfValidSamples'] < 4) | (merged_heart_rate_df['NumOfValidSamplesAfterBfill'] < 30), 'BpmMean'] = np.NaN
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$OLD FILTER$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            merged_heart_rate_df.loc[(merged_heart_rate_df['NumOfValidSamples'] <= 1) | (merged_heart_rate_df['NumOfValidSamplesAfterBfill'] <= 1), 'BpmMean'] = np.NaN

            # Rename index column
            merged_heart_rate_df.index.name = 'DateTime'

            ########## Save output CSV file to each subject output folder ##########

            # Set up the path to the subject's output folder
            subject_output_path_history = ut.output_record(OUTPUT_PATH, subject, user_name, now)
            subject_output_path = OUTPUT_PATH.joinpath(subject)
            
            if not subject_output_path_history.exists():
                subject_output_path_history.mkdir(parents=True)
                
                
            # Select specific columns to reorder the columns and save the resulting DataFrame to a CSV file
            merged_heart_rate_df[['BpmMean',
                                'NumOfValidSamples',
                                'NumOfValidSamplesAfterBfill',
                                'NumOfAllSamples',
                                'Mode']].to_csv(subject_output_path_history.joinpath(f'{subject} Heart Rate.csv')) 
            
            ut.check_for_duplications(subject_output_path, subject_output_path_history)
            
        # If there are any missing heart_rate files for any subjects, logger.info the subject IDs
        if subjects_with_missing_heart_rate_files:
            print(f'Subjects with missing heart rate files inside FITBIT/Physical Activity folder of each subject:')
            print(subjects_with_missing_heart_rate_files)
        # Create an empty list to hold any subjects that are missing HRV or respiratory files
        subjects_with_missing_steps_files = []
        full_subjects_steps_list = []
        all_subjects_steps_df = pd.DataFrame()

        print('\n Process and aggregate steps Data')
        tqdm_subjects = tqdm(os.listdir(DATA_PATH))
        for subject in tqdm_subjects:

            if run_on_specific_subjects and subject not in subjects_to_run_on:
                continue
            tqdm_subjects.set_description(f'Subject: {subject}', refresh=True)
            
            if not re.search(r'\d{3}$', subject):
                continue
            # Set up the path to the subject's sleep folder
            steps_json_directory = DATA_PATH.joinpath(f'{subject}\FITBIT\Physical Activity')
            # Find all "steps-YYYY-MM-DD.json" files in the Physical Activity folder
            steps_file_name_pattern = re.compile(r'^steps-\d{4}-\d{2}-\d{2}.json')

            steps_api_file_name_pattern = re.compile(r'^api-steps-\d{4}-\d{2}-\d{2}.json')

            steps_json_files = [file_name for file_name in os.listdir(steps_json_directory)
                                if steps_file_name_pattern.search(file_name)]

            steps_api_files = [file_name for file_name in os.listdir(steps_json_directory)
                                if steps_api_file_name_pattern.search(file_name)]
            # If the subject is missing steps files, skip them and add their name to the list
            if not steps_json_files:
                if not steps_api_files:
                    subjects_with_missing_steps_files.append(subject)
                    continue # skipping current subject

            # Sort the files by date (the date is in the file name)
            steps_json_files = sorted(steps_json_files, reverse=True)

            steps_api_files = sorted(steps_api_files, reverse=True)

            try:
                with open(OUTPUT_PATH.joinpath(subject).joinpath('steps_df_after_datetime_conversion.pkl'), 'rb') as f:
                    subject_steps_df = pickle.load(f)
            except:
                steps_file_name_pattern = re.compile(r'^steps-\d{4}-\d{2}-\d{2}.json')
                steps_api_name_pattern = re.compile(r'^api-steps-\d{4}-\d{2}-\d{2}.json')
                steps_json_files = [file_name for file_name in os.listdir(steps_json_directory)
                                    if steps_file_name_pattern.search(file_name)]
                steps_api_files = [file_name for file_name in os.listdir(steps_json_directory)
                                    if steps_api_name_pattern.search(file_name)]
                if not steps_json_files:
                    if not steps_api_files:
                        subjects_with_missing_steps_files.append(subject)
                        continue
                if steps_json_files:
                    # Iterate over the files and add them to the full list steps data of all subjects
                    steps_json_files = sorted(steps_json_files, reverse=True)
                    all_steps_files_df = pl.DataFrame()
                    for json_steps_file in steps_json_files:
                        file_df = pl.read_json(os.path.join(steps_json_directory, json_steps_file))
                        all_steps_files_df = pl.concat([all_steps_files_df, file_df])
                    
                    # convert the 'dateTime' column to datetime
                    subject_steps_df = (
                        all_steps_files_df
                        .with_columns(
                            pl.col('dateTime')
                            .str.strptime(pl.Datetime, '%m/%d/%y %H:%M:%S')
                            .dt.convert_time_zone('Israel')
                            .dt.replace_time_zone(None)
                            .dt.cast_time_unit('ns'),
                            value=pl.col('value').cast(pl.Int64)
                        )
                        .to_pandas()
                    )

                    with open(OUTPUT_PATH.joinpath(subject).joinpath('steps_df_after_datetime_conversion.pkl'), 'wb') as f:
                        pickle.dump(subject_steps_df, f)
                elif steps_api_files:
                    steps_api_files = sorted(steps_api_files, reverse=True)
                    subject_steps_list = []
                    for json_file in steps_api_files:
                        with open(steps_json_directory.joinpath(json_file)) as f:
                            # json to dict
                            subject_steps_list.extend(json.load(f))
                    # Convert the list of dictionaries to a dataframe
                    subject_steps_df = pd.json_normalize(subject_steps_list)

                    # convert the 'dateTime' column to datetime
                    subject_steps_df['dateTime'] = pd.to_datetime(subject_steps_df['dateTime'])

                    with open(OUTPUT_PATH.joinpath(subject).joinpath('steps_df_after_datetime_conversion.pkl'), 'wb') as f:
                        pickle.dump(subject_steps_df, f)
                

            tqdm_subjects.set_description(f'Subject: {subject}', refresh=True)
            relevant_subject_steps_df = subject_steps_df
            if relevant_subject_steps_df.shape[0] == 0:
                subjects_with_missing_steps_files.append(f'{subject} is missing steps files')
                continue
            # Remove dates that are not in the range of the experiment
            subject_dates_of_experiment = ut.get_subject_dates_of_experiment(subject, METADATA_PATH)
            # Select only the dates that are in the range of the experiment dates
            relevant_subject_steps_df = relevant_subject_steps_df[
                relevant_subject_steps_df['dateTime'].between(subject_dates_of_experiment.iloc[0]['ExperimentStartDateTime'],
                                                            subject_dates_of_experiment.iloc[0]['ExperimentEndDateTime'])]
            
            # If the subject is missing steps data/files, add their name to the missing files list
            if len(relevant_subject_steps_df) == 0:
                subjects_with_missing_steps_files.append(subject)
            # add index to the list of valid indexes
            # valid_indexes.extend(index_of_relevant_subject_steps_df)

            # subject_steps_df = subject_steps_df.loc[valid_indexes]
            
            relevant_subject_steps_df = relevant_subject_steps_df.rename(columns={'dateTime': 'DateAndMinute',
                                                                'value': 'StepsInMinute'})
            
            relevant_subject_steps_df = relevant_subject_steps_df[['DateAndMinute', 'StepsInMinute']].sort_values('DateAndMinute')
            
            # Save output CSV file to Output folder
            subject_output_path_history = ut.output_record(OUTPUT_PATH, subject, user_name, now)
            subject_output_path = OUTPUT_PATH.joinpath(subject)
            
            if not subject_output_path_history.exists():
                subject_output_path_history.mkdir(parents=True, exist_ok=True)
                
            relevant_subject_steps_df.to_csv(subject_output_path_history.joinpath(f'{subject} Steps.csv'))
            
            ut.check_for_duplications(subject_output_path, subject_output_path_history)
            
        if subjects_with_missing_steps_files:
            print(f'Subjects with missing or not relevant dates of FITBIT/Physical Activity/steps.json file:')
            print('\n'.join(subjects_with_missing_steps_files))
            print('Change/Delete the missing files and run the script again')
        
        subjects_with_missing_steps_files = []
        full_subjects_steps_list = []
        subject_steps_list = []
        all_subjects_steps_df = pd.DataFrame()
        
        print('\n Aggregate steps Data')
        tqdm_subjects = tqdm(os.listdir(DATA_PATH))
        for subject in tqdm_subjects:
            if run_on_specific_subjects and subject not in subjects_to_run_on:
                continue
            tqdm_subjects.set_description(f'Subject: {subject}', refresh=True)
            if not re.search(r'\d{3}$', subject):
                continue
            
            subject_steps_path = OUTPUT_PATH.joinpath(subject).joinpath(f'{subject} Steps.csv')
            if not subject_steps_path.exists():
                subjects_with_missing_steps_files.append(subject)
                continue
            subject_steps_df = pd.read_csv(subject_steps_path)
            subject_steps_df['Id'] = [subject] * len(subject_steps_df)
            
            all_subjects_steps_df = pd.concat([subject_steps_df, all_subjects_steps_df])
            
            
        # Change the order of columns and sort
        all_subjects_steps_df = all_subjects_steps_df[['Id', 'DateAndMinute', 'StepsInMinute']].sort_values(['Id', 'DateAndMinute'])
        
        all_subjects_steps_df = concate_to_old('Steps', AGGREGATED_OUTPUT_PATH, all_subjects_steps_df)
        # Save output CSV file to Aggregated Output folder
        all_subjects_steps_df.to_csv(AGGREGATED_OUTPUT_PATH_HISTORY.joinpath(f'Steps Aggregated.csv'), index=False) 
        all_subjects_steps_df.to_parquet(AGGREGATED_OUTPUT_PATH_HISTORY.joinpath(f'Steps Aggregated.parquet'), index=False)
        ut.check_for_duplications(AGGREGATED_OUTPUT_PATH, AGGREGATED_OUTPUT_PATH_HISTORY)
        
        if subjects_with_missing_steps_files:
            print(f'Subjects with missing steps.csv file:')
            print('\n'.join(subjects_with_missing_steps_files))
            print('Change/Delete the missing files and run the script again')
        """
    , language="python",
    line_numbers=True,)



with st.expander("Example subject steps file"):
    table,code = spreadsheet(r"pages/assets/C053 Steps.csv")
    st.write(table)
    st.code(code, language="python", line_numbers=True)

with st.expander("Example subject heart rate file"):
    table, code = spreadsheet(r"pages/assets/C016 Heart Rate.csv")

    st.write(table)

    st.code(code, language="python", line_numbers=True)

st.divider()

st.subheader("Heart Rate and Steps features dictionary")

st.markdown(
    """
Here you can search for a specific features (i.e. columns) that you can find in the related files.
"""
)


features_df = (
    pl.read_csv(r"pages/assets/features_dict.csv", encoding="ISO-8859-1")
    .filter(pl.col("Page") == "Preprocess")

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
