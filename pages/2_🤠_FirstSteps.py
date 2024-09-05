import streamlit as st


st.title("First steps")

st.divider()

st.header("Lets get started!")

st.write(
    """
    Welcome to the first steps of your project! 🚀

    In this section, we will guide you through the initial steps to set up your project.

    We will cover the following topics:
    - Setting up your project Google Drive folders
    - Creating a new Subject Dates csv file
    - Creating not in Israel file
    
    """
)

st.divider()

st.header("Setting up your project Google Drive folders")

st.write(
    """
    To start your project, you will need to create a folder structure in your Google Drive.
    
    The required folder structure is the following:
    """
)

folder_structure = """
Shared drive
└── AdmonPsy - PROJECT NAME
    └── Experiment
        ├── Data 
        └── Processed Data
            └── Metadata
            
"""

st.markdown(f"```text\n{folder_structure}\n```")

st.image(
    r'pages/Screenshot 2024-09-01 094511.png'
)


st.write(
    """
    The `Data` folder will contain the raw data files from the FitBit devices.
    
    The `Processed Data` folder will contain the processed data files.
    
    The `Metadata` folder will contain the metadata about the subjects of the experiment.
        
        """

)

st.divider()

st.header("Creating a new Data folder in Google Drive")

st.write(
    """
    The `Data` folder will contain the raw data files from the FitBit devices.
    
    To create a new `Data` folder in Google Drive, follow these steps:
    
    1. Open your Google Drive.
    2. Navigate to the `AdmonPsy - PROJECT NAME` folder.
    3. Create a new folder named `Experiment`.
    4. Inside the `Experiment` folder, create a new folder named `Data`.
    5. Upload the raw data files from the FitBit devices to the `Data` folder.
    """
)

st.image(
    r'pages/Screenshot (3).png'
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

st.markdown(f"```text\n{sub_data_folder_structure}\n```")



st.divider()

st.header("Creating a new Subject Dates csv file")

st.write(
    """
    The `Metadata` folder will contain a `Subject Dates.csv` file.
    
    This file will contain the following columns:
    
    - `Id`: The subject's ID.
    - `ExperimentStartDate`: The date the experiment started.
    - `ExperimentStartTime`: The time the experiment started.
    - `ExperimentEndDate`: The date the experiment ended.
    - `ExperimentEndTime`: The time the experiment ended.
    - `Device` (Optional): The FitBit device used by the subject.
    """
)

st.image(
    r'pages/Screenshot (4).png'
)



