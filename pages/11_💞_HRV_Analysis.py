import streamlit as st

st.title("HRV Analysis Page")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'HRV Analysis' page in our app.

We will cover the following topics:
1. How to extract the HRV data for all subjects.
2. How to review the extracted HRV data files.
"""
)

st.divider()

st.header("1. How to extract the HRV data for all subjects?")


dependencies_container = st.container(border=True)

dependencies_container.markdown(
    """
    Before you run the extract HRV script, ensure that you have the following:
    - Sleep All Subjects csv file after the 'Extract Sleep Data' step.
    - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
    - sleep json files for all the subjects you want to extract the HRV data for in the 'Data' folder (after the set up step). 1 file for each month (from 1st to 30th).
    - * Computed Temperature csv files in the data folder after the 'set up' step. 1 file for each month (from 1st to 30th).
    - Daily Respiratory Rate Summary csv files in the data folder after the 'set up' step. 1 file for each day of the experiment.
    - Heart rate Variability Details csv files in the data folder after the 'set up' step. 1 file for each day of the experiment.
    - Device Temperature csv files in the data folder after the 'set up' step. 1 file for each day of the experiment.

    * Not mandatory, but it is recommended to have the computed temperature csv files in the data folder for full output files.
    """
)


st.markdown(
    """
The 'HRV Processing' page in our app is where we process the raw HRV, Temperature, and Respiration raw data files for all subjects in the project.

For this step, we need to ensure that we 

To extract the HRV, temperature and respiratory data for all subjects, follow these steps:

1. Open the app.

2. Click on the 'HRV' tab.

3. Load your project by selecting the project and clicking on the 'Load' button.

4. Wait for the app to load HRV data table.

5. Review the table to ensure that each subject has a reasonable number of records from each mandatory files, as described above.

6. By selecting subjects from the table and click on the 'Show available data' button, you can see the available data files for the selected subjects.

"""
)

st.image(
    r"pages/Screenshot 2024-10-19 173716.png"
)


st.markdown(
    """
7. Filter the subjects by checking or unchecking the boxes of the 'run' column.
"""
)

st.image(
    r"pages/Screenshot 2024-10-19 173809.png"
)

st.markdown(
    """
8. Click on the 'Run HRV Processing' button to run the HRV processing script.
"""
)

st.image(
    r"pages/Screenshot 2024-10-19 173857.png"
)

st.markdown(
    """
9. After the HRV processing is started, a black window will appear with the progress of the processing.
"""
)


st.image(
    r"pages/Screenshot 2024-10-19 173948.png"
)

st.markdown(
    """
10. After the processing is finished, the black window will close, and the HRV data will be saved in the project output folder.
"""
)

st.divider()

st.header("2. How to review the extracted HRV data files?")
