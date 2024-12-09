import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(
    page_title="First steps",
    page_icon="🤠",
    layout="wide",
)



st.title("First steps")



st.divider()

st.title("Introduction")

st.markdown(
    """
In this step you will create the project folder, necessary files (subjects Dates, not in Israel) and raw data folder – **project maintainer help is required** for this step (usually lab programmer). This is a very important step that makes sure the code will run properly and smoothly. Note that due to differences in downloading methods (API, old website download, google takeouts) that changed since Google bought Fitbit the content and structure of these folders might differ, but the relevant files should be roughly the same. At the “set up” section we will run a script that unifies different downloading methods into one format. Below we present two methods to *manually* download the folders, but there could be changes in the methods and steps in the future (thanks, Google). Besides changes in folder structure, data files might change as well. <u>**Thus, any changes made by Google\Fitbit in data structure should be carefully integrated by future developers.**</u>
    
    """, unsafe_allow_html=True
)

intro_container = st.container(border=True)

intro_container.markdown(
    """
It is also possible to AUTOMATICALLY download Fitbit data using API. The section “download API” explains how to do it.  
"""
)

st.markdown(r"""
            

Currently, the code assumes that - 
            
1. A project folder is created in a shared drive folder shared with the project maintainer account. 
            
2.	Folders’ hierarchy are EXACTLY as described below.
                        
3.	Subjects’ dates (a .csv file containing records of the time range in which the subjects wore the Fitbit device) is stored in a file name “Subjects Dates.csv”
                        
4.	What happens if subjects are not in Israel during part of the measuring period? Generally, it is best to avoid measuring subjects when they are not in Israel due to time zone differences. Fitbit does not store information on timezone, so measuring subjects outside of israel can cause timestamps problems. But if subjects are not in Israel during the time of measurement it is possible to record the times (up until 2 periods) in a different file called “not in israel.xlsx”. 

:red[Note:]  The code will ignore days where the subject is not in Israel when calculating daily and grand average features but will keep data in the 1-minute resolution file (sub_0001 Heart Rate and Steps and Sleep Aggregated.csv) as well as in the “Sleep All Subjects.csv” file. Thus users can decide whether to use it for their own calculations. 
            
"""
            )
st.divider()

with st.expander("1. Setting up your project Google Drive folders"):

    st.write(
        """
        To start your project, you will need to create a specific folder structure in your Google Drive shared folder (i.e. project's folder).
        
        Your folder structure should look like this:
        """
    )



    folder_structure = """
    Shared drive
    └── PROJECT NAME
        └── Experiment
            ├── Data 
            └── Processed Data
                └── Metadata
                
    """

    st.markdown(f"```text\n{folder_structure}\n```")

    st.write(
        """
        For example:
        """
    )

    st.image(
        r'./pages/assets/Screenshot 2024-09-01 094511.png'
    )



    st.markdown(
        """
        The `AdmonPsy - PROJECT NAME` folder is the main folder for your project (PROJECT NAME = the name of your project).

        The `Experiment` folder is the code "environment" for your project. It will contain the following subfolders:

            The `Data` folder will contain the raw data files from the FitBit devices (more details in section 2).
        
            The `Processed Data` folder will contain the processed data files (after runing the scripts int the next stages).
        
            The `Metadata` folder will contain the metadata about the subjects of the experiment (more details in sections 3-4).
            
            """

    )

st.divider()

with st.expander("2. Downloading raw data."):


    st.markdown(
        r"""
    In this section you will download the subject's raw data and store it in the raw data folder (simply called “data”). We begin by an explanation on the data folder structures followed by two methods to *manually* download the Fitbit raw data – one using google takeouts (relevant to @gmail.com accounts) and the old download relevant to non-Gmail accounts and will probably be deprecated soon. Thus, the google takeout method is the one relevant to new studies.


    :red[Note:] If you wish to download the data AUTOMATICALLY skip this step and move to download API section.
    """
    )


    st.header("The Data folder")

    st.write(
        """
        The `Data` folder will contain the raw data files from the FitBit devices.

        In the set up step, the script will read the raw data files from the `Data` folder filter the necessary files by the name of the files and move them to the `Data` folder in the 'Processed Data' folder.

        """
    )

    note_container = st.container(border=True)
    note_container.markdown(
        """
        * The names of the files and folders that we will create in the steps below need to be **exactly** as written in the instructions.
        * The names of the files and folders are **case-sensitive**.
        """
    )

    st.header("Instructions for google account")

    st.subheader("If your subject has a google account with the form of {subject name}@gmail.com")

    st.markdown(
        """
    1. Open your browser (Chrome, Firefox, etc.) and go to https://takeout.google.com/
    2. Sign in with your fitbit google account.
    3. Click on "Deselect all".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 184452.png'
    )


    st.markdown(
        """
    4. Scroll down and select "Fitbit".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 184653.png'
    )

    st.markdown(
        """
    5. Click on "Next step".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 184747.png'
    )

    st.markdown(
        """
    6. Select the file destination to google drive (i.e. add to drive).
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 185010.png'
    )

    st.markdown(
        """
    7. Select the frequency of the export (i.e. every 2 months or one time).
    8. Select the file type to ".zip".
    9. Click on "Create export" (i.e. sometimes you would be required to enter your google password again).
    10. Wait for the export to be ready.
    11. Go to your google drive and find the file that you just exported under the name "takeout-{some long number}.zip" and download it. 
        
        :red[Note:] The file will be on the root of your google drive and sometimes in one export there would be more then one zip file, its important to download all of them.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190037.png'
    )

    st.markdown(
        """
    12. go back to your project folder.
    13. Create a new folder called "Data" (case sensitive) if it doesn't exist.
    14. Open the "Data" folder and create a new folder with the name of your subject. The name should be "{subject group}_{subject number as 3 digit number}" (e.g. "sub_000" or "C_019").
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190230.png'
    )


    st.markdown(
        """
    15. Open the folder you just created and upload the zip file that you downloaded in step 11.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190522.png'
    )


    st.markdown(
        """
    16. Right click on the zip file and select "Extract here".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190615.png'
    )

    st.markdown(
        """
    17. Delete the zip file.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190643.png'
    )

    st.markdown(
        """
    18. You are done! 🎉
        """
    )

    st.divider()

    st.header("Instructions for fitbit account")

    st.subheader("If your subject has a fitbit account with the form of {subject name}@labs.hevra.haifa.ac.il")

    st.markdown(
        """
    1. Open your browser (Chrome, Firefox, etc.) and go to https://fitbit.com/settings and sign in with your fitbit account.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190824.png'
    )

    st.markdown(
        """
    2. Click on "Data Export".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 191238.png'
    )

    st.markdown(
        """
    3. Click on "Request Data".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 191313.png'
    )

    st.markdown(
        """
    4. Sometimes you would be required to confirm your email address after clicking on "Request Data".
    5. Wait for the 'Download' button to be available. You can refresh the progress with the refresh button to see the progress.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 191606.png'
    )

    st.markdown(
        """
    6. Click on "Download".
    7. Go to your project's google drive and open the "Experiment" folder.
    8. Create a new folder called "Data" (case sensitive) if it doesn't exist.
    9. Open the "Data" folder and create a new folder with the name of your subject. The name should be "{subject group}_{subject number as 3 digit number}" (e.g. "sub_000" or "C_019").
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 190230.png'
    )

    st.markdown(
        """
    10. Open the folder you just created and upload the zip file that you downloaded in step 6.
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 192932.png'
    )

    st.markdown(
        """
    11. Right click on the zip file and select "Extract here".
    """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 192959.png'
    )

    st.markdown(
        """
    12. Delete the zip file.
    13. You are done! 🎉
        """
    )

st.divider()

with st.expander("Subfolder structure"):

    st.write(
        """
        The `Data` folder will contain a subfolders for each subject in the experiment.
        The subfolder structure looks different for google account and fitbit account.


        But in general, there will be few specific files that are required for generating the processed data files.
        """
    )


    st.image(
        r'pages/assets/Screenshot (3).png'
    )

    sub_data_folder_structure = """
    Data 
    └── sub_000
        └── FITBIT
            ├── Sleep
            |   ├──Computed Temperature - 2023-12-01.csv (per month)
            |   ├──Daily Heart Rate Variability Summary - 2023-12-25.csv (per day)
            |   ├──Daily Respiratory Rate Summary - 2023-12-25.csv (per day)
            |   ├──Device Temperature - 2023-12-14.csv (per day)
            |   ├──Heart Rate Variability Details - 2023-12-25.csv (per day)
            |   ├──Respiratory Rate Summary - 2023-11-30.csv (per month)
            |   └──sleep-2023-11-29.json (per month)
            ├── Stress 
            |   ├──Mindfulness Eda Data Sessions.csv (per all experiment)
            |   └──Mindfulness Sessions.csv (per all experiment)
            └── Physical Activity
                ├── heart_rate-2023-12-14.json (per day)
                └── steps-2023-12-14.json (per day)
    """


    st.subheader("Fitbit account")

    st.markdown(f"```text\n{sub_data_folder_structure}\n```")

    sub_data_folder_structure_google = """
    Data
    └── sub_000
        └── Takeout
            └── Fitbit
                ├── Global Export Data
                |   ├── sleep-2023-11-29.json (per month)
                |   ├── heart_rate-2023-12-14.json (per day)
                |   └── steps-2023-12-14.json (per day)
                ├── Heart Rate Variability
                |   ├── Daily Heart Rate Variability Summary - 2023-12-25.csv (per day)
                |   └── Heart Rate Variability Details - 2023-12-25.csv (per day)
                ├── Temperature
                |   ├── Computed Temperature - 2023-12-01.csv (per month)
                |   └── Device Temperature - 2023-12-14.csv (per day)
                └── Mindfulness
                    ├── Mindfulness Eda Data Sessions.csv (per all experiment)
                    └── Mindfulness Sessions.csv (per all experiment)

    """

    st.subheader("Google account")

    st.markdown(f"```text\n{sub_data_folder_structure_google}\n```")



                



st.divider()

with st.expander("3. Creating a new Subject Dates csv file"):


    st.write(
        """
        The `Subject Dates` csv file will contain the dates of the experiment for each subject.
        The file will be used to filter the raw data files and to generate the processed data output files in the next steps.

        The `Subject Dates` csv file should be located in the `Metadata` folder in the `Processed Data` folder.

        The `Subject Dates` csv file should contain the following columns:
        - `Id` - the subject's ID (e.g. sub_000).
        - `ExperimentStartDate' - the start date of the experiment for the subject (e.g. 03/01/2023).
        - `ExperimentStartTime' - the start time of the experiment for the subject (e.g. 09:00).
        - `ExperimentEndDate' - the end date of the experiment for the subject (e.g. 03/02/2023).
        - `ExperimentEndTime' - the end time of the experiment for the subject (e.g. 09:00).
        - `Device' - the email address of the subject's account (gmail or fitbit user).
        - `Group' - the group of the subject (e.g. C or T). (Optional)
        - `Token' - the token of the subject API (Optional)
        """
    )



    st.subheader("Subject Dates file example")

    subdates = pd.read_csv("pages/assets/Subjects Dates.csv").head(8)

    st.write(subdates)


st.divider()
with st.expander("4. Creating a new not in Israel file"):

    st.write(
        """
        The `not in Israel` excel (.xlsx) file will contain the dates where the subject was not in Israel.

        The file will be used to filter the raw data files and to generate the processed data output files in the next steps.

        The `not in Israel` excel (.xlsx) file should be located in the `Experiment` folder in the project's folder.

        The `not in Israel` excel (.xlsx) file should contain the following columns:
        - `Id` - the subject's ID (e.g. sub_000).
        - `היה בחו"ל? בזמן המדידה של השעון?` - a binary column that indicates if the subject was not in Israel during the experiment (לא/כן).
        - `start_date` - the start date of the subject not being in Israel (e.g. 2023-12-01).
        - `end_date` - the end date of the subject not being in Israel (e.g. 2023-12-02).
        - `state` - the state where the subject was in Hebrew (e.g. גרמניה).
        - `start_date_1` - the start date of the subject not in Israel in the second period (e.g. 2023-12-03).
        - `end_date_1` - the end date of the subject not in Israel in the second period (e.g. 2023-12-04).
        - `state_1` - the state where the subject was in Hebrew in the second period (e.g. גרמניה).
        """
    )

    notInIsrael = pd.read_excel("pages/assets/not_in_israel_df.xlsx", sheet_name='participants').head(8)

    st.write(notInIsrael)

st.divider()

with st.expander("5. Update your project settings in the app"):

    st.write(
        """
        The last step is to update your project settings in the app. The app is installed in a designated computer located in our lab.

        The settings will include the following information:
        - The name of the project.
        - The path to the 'Data' folder in the 'Experiment' folder, where the raw data files are located.
        - The path to the 'Processed Data' folder in the 'Experiment' folder, where the processed data files will be saved.
        """
    )

    st.subheader("Instructions")

    st.markdown(
        """
        1. Open the app.
        """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 200217.png'
    )

    st.markdown(
        """
        2. Click on the 'Settings' tab.
        """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 200351.png'
    )

    st.markdown(
        """
        3. Select the option of NEW project.
        """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 200536.png'
    )

    st.markdown(
        """
        4. Fill in the project name.
        5. Copy the path of the 'Data' folder in the 'Experiment' folder.
        6. Copy the path of the 'Processed Data' folder in the 'Experiment' folder.
        """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 200641.png'
    )


    st.markdown(
        """
        7. Click on 'Save'.
        8. You are done! 🎉
        """
    )

    st.image(
        r'pages/assets/Screenshot 2024-10-11 200803.png'
    )

st.divider()


