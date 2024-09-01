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
        ├── Processed Data 
        └── Data
            └── Metadata
            
"""

st.markdown(f"```text\n{folder_structure}\n```")

st.image(
    r'Screenshot 2024-09-01 094511.png'
)