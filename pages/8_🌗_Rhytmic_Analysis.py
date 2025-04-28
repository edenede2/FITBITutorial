import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import polars as pl



st.set_page_config(
    page_title="Rhytmic Analysis",
    page_icon="🌗",
    layout="wide",
)


st.title("Rhytmic Analysis Step")


st.divider()


st.header("Introduction")

st.markdown("""
## Introduction:
            
In the rhythmic analysis section, a parametric circadian rhythm model called “cosinor model” is
fitted to a selected signal from the 1-minute resolution file. The goal is to fit the model and
extract different parameters of the model to be used in further analyses. 
For additional information on cosinor analyses see:
            
Cornelissen, G. (2014). Cosinor-based rhythmometry. Theoretical Biology and Medical
Modelling, 11, 1-24.‏
The code is a wrapper around the ‘CosinorPy’ package, so for specific variables documentation
see:
https://github.com/mmoskon/CosinorPy

            
in the app, you can modify several parameters:
    1. Include \ omit not in israel = TRUE and dst change = TRUE (default: omit)
            
    2. Window size (to how many days the cosinor data is fitted each time, default: 24 hours)
    
    3. Windows overlap (default: 24 hours)
    
    4. Down sampling threshold (default: 5 minute)
    
    5. Missing data threshold total of missing data allowed per day (default: 37%)
    
    6. Largest missing data gap allowed per window (default: 37%)
    
    7. Data interpolation (default: no)
    
    You can always start with the default settings and modify according project specific
    requirements.

Analyses pipeline:
            
    1. Omit dates of not_in_israel = TRUE, and is_ds_change = TRUE
    
    2. Filter data from first to last available midnight (days when the subject receive the watch
    and days when the subject return the watch are omitted)
    
    3. Create windows for analysis between start and end date of the experiment, based on
    user desired settings (window size, window overlap)
    
    4. For each window, count number of missing data points + largest missing data points gap
    
    5. Omit days with number of missing data larger than threshold and days with missing data
    gap larger than threshold.
    
    6. Down sample signal based on user settings (period) (default: 5 minutes)
    
    7. If interpolation = TRUE, interpolate remaining missing data
    
    8. Perform cosinor analysis per down sampled window using the cosinor.fit_me function
    from cosinorPY package.
    
    a. To understand the output, check documentation for this function in:
    https://github.com/mmoskon/CosinorPy/blob/master/docs/docs_cosinor.md
    
    9. Store cosinor parameters per window and aggregated across all windows. Store user
    settings (for reproducibility) as columns in the output .csv files.
            

            """, unsafe_allow_html=True)