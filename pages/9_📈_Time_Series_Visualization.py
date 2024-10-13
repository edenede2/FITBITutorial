import streamlit as st

st.title("Time Series Visualization")


st.divider()

st.header("Introduction")

st.markdown(
    """
In this page, we will discuss the 'Time Series Visualization' page in our app.

We will cover the following topics:
1. What is the 'Time Series Visualization' page?
2. How do we load the 'Time Series Visualization' page?
3. How do we control the plots in the 'Time Series Visualization' page?
"""
)

st.divider()

st.header("1. What is the 'Time Series Visualization' page?")

st.markdown(
    """
The 'Time Series Visualization' page in our app is where we visualize the time series data from the 1 minute resolution file of all the subjects in the project.

The time series data should help us to understand the behavior of the signals over time for each subject with different filters from the 1 minute resolution file.

The time series plots should help us to identify any patterns or anomalies in the data that we can use to further analyze the data.

The time series plots include the following:

1. StepsInMinute: The number of steps taken by the subject in each minute.

2. BpmMean: The mean heart rate of the subject in each minute of the experiment (without the missing values).

3. Sleeping: A binary variable that indicates whether the subject is sleeping or not in each minute of the experiment.

4. Sleep Stages: The sleep stages of the subject in each minute of the experiment.

5. Feature: The visualization of the 'Feature' column in the 1 minute resolution file. It shows the categorical values of the 'Feature' column in the data for each minute.

6. ValidSleep: A binary variable that indicates whether the subject is in a valid sleep or not in each minute of the experiment.

7. Weekend: A binary variable that indicates whether the day is a weekend or not in each minute of the experiment.

8. Outliers: A binary variable that indicates whether the bpm value in the specific minute is identified as an outlier or not for the specific feature.

9. Not in IL: A binary variable that indicates whether the subject is in Israel at the specific minute or not.

"""
)

st.image(
    r"pages/Screenshot 2024-10-12 195712.png"
)

st.divider()

st.header("2. How do we load the 'Time Series Visualization' page?")

st.markdown(
    """
1. Open the app from your desktop.

2. Click on the 'Time Series Visualization' tab.

3. Select your project from the dropdown menu and click on the 'Load' button.

4. Check or uncheck the boxes of the subjects that you want to visualize, and click on the 'Show Selected' button to visualize the time series data for the selected subjects.

:red[Note:] The plots in this page are very heavy. Please don't select more then 10 subjects at a time.
"""
)

st.image(
    r"pages/Screenshot 2024-10-12 195352.png"
)

st.markdown(
    """
5. Now, you can see the time series plots for the selected subjects.
"""
)

st.image(
    r"pages/Screenshot 2024-10-12 195509.png"
)

st.divider()

st.header("3. How do we control the plots in the 'Time Series Visualization' page?")

st.markdown(
    """
The plots in the 'Time Series Visualization' enable you to select the specific time series data that you want to visualize.

You can display or hide the specific time series data by clicking on the legend of the plot.

"""
)

st.image(
    r"pages/Screenshot 2024-10-12 195816.png"
)



st.markdown(
    """
You can also zoom in on the plot by selecting the specific area that you want to zoom in on.

"""
)


st.image(
    r"pages/Screenshot 2024-10-12 195925.png"
)

st.image(
    r"pages/Screenshot 2024-10-12 200013.png"
)



st.markdown(
    """
You can also reset the plot by clicking on the 'Reset axes' button in the corner of the plot.
    
    """
    )

st.image(
    r"pages/Screenshot 2024-10-12 200114.png"
)

st.markdown(
    """
You can also download the plot as a PNG file by clicking on the 'Download plot as PNG' button in the corner of the plot.

"""
)

st.image(
    r"pages/Screenshot 2024-10-12 200200.png"
)

st.markdown(
    """
You can also isolate the specific time series data by clicking on the legend of the plot twice.
    
    """
    )

st.image(
    r"pages/Screenshot 2024-10-12 200334.png"
)

st.divider()

