import streamlit as st

st.title("Set up your processed data folder")

st.divider()

st.header("Let's get started!")

st.write(
    """
    In this section, we will guide you through the initial steps to set up your processed data folder.
    
    We will cover the following topics:
    1. Run the setup script.
    2. Validate the folder structures.
    """

)

st.divider()

st.header("1. Run the setup script")

st.write(
    """
    To set up your processed data folder, you will need to run the set up script.

    The script will create the necessary folder structures for your processed data.
    """
)

st.subheader("Instructions")

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
    2. Click on the 'set up' tab.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 201622.png"
)

st.write(
    """
    3. Load your project by selecting the project and clicking on the 'load' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 201647.png"
)

st.write(
    """
    4. Enter your name in the 'name' field.
    5. Review the table that shows the available subjects.
       :red[Note: The table should show the subjects that are available in your 'Data' in the 'Experiment' folder.]
       :red[You can see the subjects that are available, there available data files, and if they are included in the subjects dates file that we made in the previous step.]
    """
)

st.image(
    "pages/Screenshot 2024-10-11 202639.png"
)

st.image(
    "pages/Screenshot 2024-10-11 202701.png"
)

st.write(
    """
    6. When you are ready, click on the Initialize data folder button. You can run only on specific subjects by selecting them in the table or initialize for all the subjects in the table.
    7. After the script is started, you can see the progress in the black window that will appear.
"""
)

st.image(
    "pages/Screenshot 2024-10-11 202753.png"
)

st.write(
    """
    8. When the script is finished, the black window will close, and you can see the message that the script is finished.
    """
)

st.divider()

st.header("2. Validate the folder structures")

st.write(
    """
    After running the setup script, you should validate the folder structures to ensure that the processed data folder is set up correctly.
    You should see the following folders:
    - 'Data' folder in the 'Processed Data' folder with all the subjects that you have initialized. Each subject should have the same structure as the 'Data' folder in the 'Experiment' folder for the fitbit accounts, and each should include only the necessary files.
    - 'Outputs' folder in the 'Processed Data' folder. It should be empty at this point. Once you start processing the data, the outputs will be saved in this folder.
    """
)


