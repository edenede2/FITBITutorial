import streamlit as st



st.set_page_config(
    page_title="Stats Visualization",
    page_icon="📊",
    layout="wide",
)

st.title("Stats Visualization")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'Stats Visualization' page in our app.

We will cover the following topics:
1. What is the 'Stats Visualization' page?
2. How do we load the 'Stats Visualization' page?
3. How do we interpret the plots in the 'Stats Visualization' page?
"""
)

st.divider()

with st.expander("1. What is the 'Stats Visualization' page?"):

    st.markdown(
        """
    The 'Stats Visualization' page in our app is where we visualize the statistics of the missing values for the combined file from the 'Combined File Generation' step.

    The statistics was calculated from the 1 minute resolution file of all the subjects in the project.

    The statistics should help us to understand the amount of missing values that we have for each subject and the behavior of the missing values in the data for each subject.

    """
    )

st.divider()

with st.expander("2. How do we load the 'Stats Visualization' page?"):

    st.markdown(
        """
    1. Open the app from your desktop.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-11 200217.png"
    )

    st.markdown(
        """
    2. Click on the 'Stats Visualization' tab.

    3. Select your project from the dropdown menu and click on the 'Load' button.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 163057.png"
    )

    st.markdown(
        """
    4. After the table is loaded, you can see the subjects that have been processed in the 'Combined File Generation' step.
    5. Select the subject that you want to visualize by checking or unchecking the box in the 'Show' column.
    6. Click on the 'Show Selected' button to visualize the statistics for the selected subjects.

    :red[Note:]
    - You can select multiple subjects.
    - You can also select the 'Show All' button to visualize the statistics for all the subjects in the 1 minute resolution file. But, it may take some time to load the statistics for all the subjects.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 163330.png"
    )


    st.markdown(
        """
    7. Now, you can see the statistics for all the selected subjects.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 183841.png"
    )


st.divider()

with st.expander("3. How do we interpret the plots in the 'Stats Visualization' page?"):

    st.markdown(
        """
    The 'Stats Visualization' page shows the following plots:
    1. The amount of gaps in the heart rate data by the size of the gap in minutes and the number of gaps with that size.
    2. The percentage of missing heart rate data for each day of experiment with the mean percentage of missing data for all of the days.
    3. The percentage of missing sleep data for all the days of experiment.
    """
    )

    st.subheader("1. The amount of gaps in the heart rate data")

    st.markdown(
        """
    In this plot, we can see in the y-axis the size of each gap (in minutes) that was found in the 1 minute resolution file of the selected subjects. The x-axis shows the number of gaps with that size.

    By looking at this plot, we can understand the distribution of the gaps in the heart rate data for the selected subjects. We can see if there are any patterns in the gaps, such as a high number of gaps with a specific size.

    For example, if we see a high number of gaps with small size of 1 to 2 minute, it may be normal, but if its a very high number of gaps with that size, it may be an indication that there are a problem with the way the data was collected or processed.

    On the other hand, if we see a high number of gaps with a very large size, it may be an indication that there are long periods of missing data in the heart rate data or that the subject was not wearing the device for a long time.
    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 184651.png"
    )

    st.subheader("2. The percentage of missing heart rate data for each day of experiment")

    st.markdown(
        """
    In this plot, we can see the percentage of missing heart rate data for each day as function of the day of the experiment. The x-axis shows the dates of the experiment and the y-axis shows the percentage of missing data for that day.

    If we put the mouse over a specific bar, we can see the exact percentage of missing heart rate samples for that day, the total number of minutes in that day and the number of missing samples.

    By looking at this plot, we can understand the behavior of the missing heart rate data for each day of the experiment. We can see if there are any patterns in the missing data, such as a high percentage of missing data for specific days or a low percentage of missing data for a sequence of days as some kind of baseline.

    For example, if we see a high percentage of missing data for a sequence of days, it may be an indication that the subject was not wearing the device for that period or that there are problems with the data collection or processing.

    On the other hand, if we see a persistent low to medium percentage of missing data for all the days, it may be an indication that there are some problems with the data collection or processing that need to be addressed by looking at the raw data or the processing steps.

    The mean percentage of missing data for all the days is shown as a horizontal line in the plot. This line can help us to understand the overall behavior of the missing data for the selected subjects.

    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 185638.png"
    )

    st.subheader("3. The percentage of missing sleep data for all the days of experiment")

    st.markdown(
        """
    In this plot, we can see the percentage of missing sleep data for all the days of the experiment. The blue part of the circle shows the percentage of existing sleep data and the red part shows the percentage of missing sleep data.

    The calculation of the percentage of missing sleep data is done by dividing the number of days without sleep data by the total number of days in the experiment.

    By looking at this plot, we can understand the behavior of the missing sleep data for all the days of the experiment. We can see if a specific subject has a high percentage of missing sleep data or if all the subjects have a similar percentage of missing sleep data.

    For example, if we see a high percentage of missing sleep data for a specific subject, it may be an indication that there are problems with the sleep data collection or processing for that subject.

    """
    )

    st.image(
        r"pages/assets/Screenshot 2024-10-12 191238.png"
    )


st.divider()

