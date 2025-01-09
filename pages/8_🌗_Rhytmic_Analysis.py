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

In the rhythmic analysis section, a parametric circadian rhythm model called “cosinor model” is fitted to a selected signal from the 1-minute resolution file. The goal is to fit the model and extract different parameters of the model to be used in further analyses. For additional information on cosinor analyses see: 
            
- Cornelissen, G. (2014). Cosinor-based rhythmometry. <i> Theoretical Biology and Medical Modelling, 11, 1-24, 16.</i>
            

The code is a wrapper around the 'CosinorPy' package, so for specific variables documentation see:
            
<a href="https://github.com/mmoskon/CosinorPy" target="_blank"> CosinorPy documentation</a>
            


In the app, you can modify several parameters:
            
1. Include \ omit not in Israel and dst (daylight saving time) dates, the default is to omit.
            
2. Window size (to how many days the cosinor data is fitted each time, default is 24 hours).
            
            """, unsafe_allow_html=True)