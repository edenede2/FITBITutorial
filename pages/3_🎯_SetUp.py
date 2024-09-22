import streamlit as st

st.title("Set up your processed data folder")

st.divider()

st.header("Let's get started!")

st.write(
    """
    In this section, we will guide you through the initial steps to set up your processed data folder.
    
    We will cover the following topics:
    - Validate the folder structure.
    - Run the setup script.
    """

)

st.divider()

st.header("Validate the folder structure")

st.write(
    """
    Before running the setup script, make sure that you have the following folder structure in your Google Drive:
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

st.write(
    """
    Now, let's make sure that the `Data` folders of each subject are in the correct structure.
    """
)

st.write(
    """
    The `Data` folder should be structured as follows:
    """
)

subject_data_structure = """
Data
└── "Subject ID"
    └── FITBIT
        ├── Physical Activity
        ├── Sleep
        └── Stress
"""

st.markdown(f"```text\n{subject_data_structure}\n```")

st.image(
    r'pages/Screenshot 2024-09-22 161020.png'
)
st.divider()

st.image(
    r'pages/Screenshot 2024-09-22 161036.png'
)
st.divider()

st.image(
    r'pages/Screenshot 2024-09-22 161102.png'
)
st.divider()


st.write(
    """
    Note: that The `Physical Activity`, `Sleep`, and `Stress` folders are the only crucial folders! 🎈
    These folders should contain the raw data files from the FitBit devices.
    """
)

