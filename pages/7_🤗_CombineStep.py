import streamlit as st

st.title("Combined File Generation Step")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'Combined File Generation' step in our pipeline.
We will cover the following topics:
1. What is the 'Combined File' ?
2. How do we run the 'Combined File Generation' step?
3. How we validate the 'Combined File Generation' step?
"""
)

st.divider()

st.header("1. What is the 'Combined File' ?")

st.markdown(
    """
After the 'Extract Sleep Data' step and the 'Preprocessing' step, we have the processed data from the sleeps, heart rate, and steps json files.

In the 'Combined File Generation' step, we merge, the processed data from those files, and create few new features that was calculated from the data.

Basicly, the processed data from the sleeps, heart rate, and steps json files into a single file.

After the 'Combined File Generation' step you will get the following files :

1. sub_000 Heart Rate and Steps and Sleep Aggregated.csv (the basic file for each subject)
2. All_Subjects_1_Minute_Resolution.parquet (for all the subjects in the project)
3. sub_000 Metrics of Heart Rate By Activity (exclude weekends).csv
4. sub_000 Metrics of Heart Rate By Activity.csv
5. No Weekends Summary of Heart Rate Metrics By Activity.csv
6. No Weekends All Subjects of Heart Rate Metrics By Activity.csv
7. Full Week Summary of Heart Rate Metrics By Activity.csv
8. Full Week All Subjects of Heart Rate Metrics By Activity.csv

The sub_000 Heart Rate and Steps and Sleep Aggregated.csv file is the basic file for each subject, and the other files are the concatenated files or aggregated files for each subject or all the subjects in the project.


"""
)

st.divider()


st.header("2. How do we run the 'Combined File Generation' step?")

st.markdown(
    """
1. Open the app from your desktop.
"""
)

st.image(
    "pages/Screenshot 2024-10-11 200217.png"
)

st.markdown(
    """
2. Click on the 'Combined File Generation' tab.


3. Select your project from the dropdown menu and enter your name.
"""
)

st.image(
    r"pages/Screenshot 2024-10-12 161327.png"
)

st.markdown(
    """
4. Click on the 'Load' button and wait for the table to load.
5. Review the table, check the 'Percentage of missing HR' and 'Percentage of missing Sleep' columns. If the percentage is too high, check for missing heart rate or sleep data (raw files or processed files) and try to re-run the respective steps, then refresh the table to check the percentage again.
"""
)

st.image(
    "pages/Screenshot 2024-10-12 161833.png"
)

st.markdown(
    """
6. Filter the run column by check or uncheck the box.
7. When you are ready, click on the 'Generate File' button.
"""
)

st.image(
    "pages\Screenshot 2024-10-12 161941.png"
)

st.markdown(
    """
8. After the 'Combined File Generation' step starts, a black window will appear with the progress of the step.
"""
)

st.image(
    "pages\Screenshot 2024-10-12 162126.png"
)

st.markdown(
    """
9. After the step is completed, the black window will close.
10. You can see the files in the 'Outputs' folder of your project.
"""
)

st.divider()

st.header("3. How we validate the 'Combined File Generation' step?")