import streamlit as st

st.title("Extract sleep data")


st.divider()

st.write(
    """
    In this section, we will guide you through the process of extracting your sleep data from the raw fitbit sleep data.

    We will cover the following topics:
    1. Extract sleep data for all subjects.
    2. Review the extracted data files.
    """
)

st.divider()

st.header("Instructions")


dependencies_container = st.container(border=True)

dependencies_container.markdown(
    """
    Before you run the extract sleep data script, ensure that you have the following:
    - The 'Experiment' folder with the necessary structure.
    - The 'Data' folder in the 'Processed Data' folder after running the 'set up' script.
    - The sleep json files for all the subjects you want to extract the sleep data for in the 'Data' folder (after the set up step).
    - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
    """
)


st.write(
    """
    1. Open the app.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 200217.png"
)

st.write(
    """
    2. Click on the 'extract sleep data' tab.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 214608.png"
)

st.write(
    """
    3. Load your project by selecting the project and clicking on the 'Load' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 214927.png"
)

st.write(
    """
    4. Review the table to ensure that each subject has a reasonable number of sleep records (e.g., at least 1 or 2 for a single month but more the 2 are reasonable too).
    """
)

st.image(
    "pages/Screenshot 2024-10-11 214857.png"
)

st.write(
    """
    5. You can now select the subjects for which you want to exclude by disabling the checkbox in the 'run' column.
    6. Click on the 'Generate Sleep All Subjects' button to extract the sleep data for all subjects.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 215148.png"
)

st.write(
    """
    7. After the process starts, you will see a black window that shows the progress of the process.
    8. 9 Files will be generated for all the subjects that you selected:
        - Sleep All Subjects.csv
        - Sleep Daily Details Exclude Thursday and Friday.csv
        - Sleep Daily Summary Exclude Thursday and Friday.csv
        - Sleep Daily Details Exclude Thursday.csv
        - Sleep Daily Summary Exclude Thursday.csv
        - Sleep Daily Details Exclude Friday.csv
        - Sleep Daily Summary Exclude Friday.csv
        - Sleep Daily Details Full Week.csv
        - Sleep Daily Summary Full Week.csv
    """
)

st.image(
    "pages/Screenshot 2024-10-11 215234.png"
)

st.write(
    """
    9. When the process is finished, the black window will close, and you will see the message that the process is finished.
    10. You finished the process of extracting the sleep data. Now you can move to the next step.
    """
)

st.divider()


source_code_container = st.container()

# collapsed source code
with st.expander("Click to expand the source code"):
    st.code(
        """
path = os.path.join(project_path, 'Scripts', '5_😴_Extract_Sleep_Data.py')

with open(path, 'r') as file:
    code = file.read()
        """,
        language="python",
    )