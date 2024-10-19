import streamlit as st

st.title("Steps & HR Data Preprocessing")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'preprocessing' step in our pipeline.
We will cover the following topics:
1. What is the 'preprocessing' step?
2. How do we run the 'preprocessing' step?
3. How we validate the 'preprocessing' step?
"""
)

st.divider()

st.header("1. What is the 'preprocessing' step?")

st.markdown(
    """
The 'preprocessing' step in our pipeline is where 

we clean, transform, and aggregate the heart rate and steps json files

that we have collected from the Fitbit watch in the 'set up' step.


It is important to remember that:

- The Heart Rate data is collected every 1 second by the Fitbit watch but sometimes the watch may not be able to collect the data due to various reasons.

- The Steps data is collected every 1 minute by the Fitbit watch.

However, the json files that we have downloaded from the Fitbit website may not be in the expected sample rate and may contain missing values for few minutes.

By fitbit, it is happening due to visualization purposes and to reduce the size of the data.

We found that the missing values occur in the data when the calories value is minimal for the specific day and show a default value.

:red[Note:] The steps jsons that we are downloading from the Fitbit API has :red[no missing values] and in the 'download api' step we are cleaning the json file to include the same values as the json files that we are downloading from the Fitbit website.

To change it, try to involve the programmer to change the code in the Fitbit API to include the missing values in the steps json file.

- Each heart rate json file contains the heart rate data for a specific day.

- Each steps json file contains the steps data for a specific month (starting from the 1st day of the month to the last day of the month).

- After the preprocessing step, we will have 4 csv files in sampling rate of 1 minute:
    1. sub_000_heartrate.csv
    2. sub_000_steps.csv
    3. steps.csv (for all the subjects in the aggregated folder)
    4. steps.parquet (for all the subjects in the aggregated folder)

"""
)

st.divider()

st.header("2. How do we run the 'preprocessing' step?")



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
    "pages/Screenshot 2024-10-11 200217.png"
)

st.markdown(
    """
2. Click on the 'Preprocessing' tab.
"""
)

st.image(
    "pages/Screenshot 2024-10-11 200217.png"
)

st.markdown(
    """
3. Select your project from the dropdown menu and enter your name.
"""
)

st.image(
    "pages/Screenshot 2024-10-12 154140.png"
)

st.markdown(
    """
4. Click on the 'Load' button and wait for the table to load.
5. Review the table, check for any missing hr or steps files, by clicking on specific subject and then on the 'Show available data' button.
"""
)

st.image(
    "pages/Screenshot 2024-10-12 154441.png"
)


st.markdown(
    """
6. Filter the run column by check or uncheck the box.
7. When you are ready, click on the 'Run Preprocessing Step' button.
"""
)


st.image(
    "pages/Screenshot 2024-10-12 154722.png"
)


st.markdown(
    """
8. After you click on the 'Run Preprocessing Step' button, a black window will appear with the progress of the preprocessing step.
"""
)

st.image(
    "pages/Screenshot 2024-10-12 154801.png"
)

st.markdown(
    """
9. When the preprocessing step is done, the black window will disappear.
10. You can now see the outputs files in the 'Outputs' folder of your project.
"""
)

st.divider()

st.header("3. How we validate the 'preprocessing' step?")