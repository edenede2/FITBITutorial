import streamlit as st

st.title("Extract EDA Page")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'Extract EDA' page in our app.

We will cover the following topics:
1. How to extract the EDA data for all subjects.
2. How to review the extracted EDA data files.
"""
)

st.divider()

st.header("1. How to extract the EDA data for all subjects?")


dependencies_container = st.container(border=True)

dependencies_container.markdown(
    """
    Before you run the extract eda script, ensure that you have the following:
    - Heart rate csv files after the 'Preprocessing' step.
    - 'mindfulness_eda_data_sessions.csv' and 'mindfulness_sessions.csv' files for all subjects in the 'Data' folder. (after the set up step)
    - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
    """
)


st.markdown(
    """
The 'EDA Analysis' page in our app is where we extract the EDA data for all subjects from the raw Fitbit EDA data (i.e., the mindfulness sessions).

Before we extract the EDA data, we need to ensure that we have the raw Fitbit EDA data for all subjects in the project.

:red[Note:] In the 'EDA Analysis' page, we will get a table with the raw EDA files that each subject have in the project data folder after the set up step.



To extract the EDA data for all subjects, follow these steps:

1. Open the app.

2. Click on the 'EDA' tab.

3. Load your project by selecting the project and clicking on the 'Load' button.

4. Wait for the app to load EDA data table.

5. Review the table to ensure that each subject has a reasonable number of EDA records, each subject should have 1 file for each file type (e.g., 1 mindfulness_eda_data_sessions.csv and 1 mindfulness_sessions.csv).

6. By selecting subjects from the table and click on the 'Show available data' button, you can see the available data files for the selected subjects.

"""
)

st.image(
    r"pages/Screenshot 2024-10-13 213157.png"
)


st.markdown(
    """
7. Filter the subjects by checking or unchecking the boxes of the 'run' column.
"""
)

st.image(
    r"pages/Screenshot 2024-10-13 213407.png"
)

st.markdown(
    """
8. Click on the 'Run EDA Processing' button to run the EDA processing script.
"""
)

st.image(
    r"pages/Screenshot 2024-10-13 213542.png"
)

st.markdown(
    """
9. After the EDA processing is started, a black window will appear with the progress of the processing.
"""
)


st.image(
    r"pages/Screenshot 2024-10-13 213850.png"
)

st.markdown(
    """
10. After the processing is finished, the black window will close, and the EDA data will be saved in the project output folder.
"""
)

st.divider()

st.header("2. How to review the extracted EDA data files?")
