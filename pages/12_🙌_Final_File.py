import streamlit as st

st.title("Final File Page")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'Final File' page in our app.

We will cover the following topics:
1. How to extract the Final File for all subjects.
2. How to review the extracted Final all subjects file.
"""
)

st.divider()

st.header("1. How to extract the Final File for all subjects?")


dependencies_container = st.container(border=True)

dependencies_container.markdown(
    """
    Before you run the Final File script, ensure that you have the following:
    - Sleep All Subjects csv file after the 'Extract Sleep Data' step.
    - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
    - Sleep Daily Summary Full Week csv files in the output folder after the 'Extract Sleep Data' step.
    - Full Week Summary of Heart Rate Metrics By Activity csv files in the output folder after the 'Combine Step' step.
    - * Summary of HRV Tempeture Respiratory at sleep files in the output folder after the 'HRV Analysis' step.
    - * EDA Summary files in the output folder after the 'EDA Analysis' step.

    * The files are not mandatory, but it is recommended to have them in the output folder for full output files if possible.
    """
)


st.markdown(
    """
The 'Final File' page in our app is where we aggregate the processed data from the 'Extract Sleep Data', 'Combine Step', 'HRV Analysis', and 'EDA Analysis' steps for all subjects in the project.


To extract the Final File for all subjects, follow these steps:

1. Open the app.

2. Click on the 'Final File' tab.

3. Load your project by selecting the project and clicking on the 'Load' button.

4. Wait for the app to load data table.

5. Review the table to ensure that each subject has the necessary files, as described above.

6. By selecting subjects from the table and click on the 'Show available data' button, you can see the content of the available data files for the selected subjects (here you can select more than one subject).

"""
)

st.image(
    r"pages/Screenshot 2024-10-19 174906.png"
)

st.image(
    r"pages/Screenshot 2024-10-19 175002.png"
)


st.markdown(
    """
7. Filter the subjects by checking or unchecking the boxes of the 'run' column.
"""
)

st.image(
    r"pages/Screenshot 2024-10-19 175041.png"
)

st.markdown(
    """
8. Click on the 'Run Final Processing' button to run the Final File script.
"""
)

st.image(
    r"pages/Screenshot 2024-10-19 175122.png"
)

st.markdown(
    """
9. After the Final File generating process started, a black window will appear with the progress of the processing.
"""
)


st.image(
    r"pages/Screenshot 2024-10-19 175302.png"
)

st.markdown(
    """
10. After the processing is finished, the black window will close, and the Final file will be saved in the project output folder.
"""
)

st.divider()

st.header("2. How to review the extracted Final File?")
