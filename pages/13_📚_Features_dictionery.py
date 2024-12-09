import polars as pl
import streamlit as st



st.set_page_config(
    page_title="Features Dictionery",
    page_icon="📚",
    layout="wide",
)


st.title("Features Dictionery Page")


st.divider()

st.header("Introduction")

st.markdown(
    """
Here you can search for a specific features (i.e. columns) that you can find in the files and get more information on it.
"""
)

st.divider()

features_df = (
    pl.read_csv(r"pages/assets/features_dict.csv", encoding="ISO-8859-1")

)

# create a session state to store the results dataframe
if "result_df" not in st.session_state:
    st.session_state.result_df = None

with st.form("search"):
    st.write("Search for a feature")
    text_input = st.text_input("Feature or file name").lower()
    type_of = st.radio(
        "Search by 👉",
        key="visibility",
        options=["Feature name", "File name", "Both" , "Description"],
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")


    show_results = False

    if submitted:
        if type_of == "Feature name":
            result_df = (
                features_df
                .filter(
                    pl.col("Feature").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )
        elif type_of == "File name":
            result_df = (
                features_df
                .filter(
                    pl.col("File").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )

        elif type_of == "Both":
            result_df = (
                features_df
                .filter(
                    pl.col("Feature").str.to_lowercase().str.contains(text_input, strict=False)
                    | pl.col("File").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )
        elif type_of == "Description":
            result_df = (
                features_df
                .filter(
                    pl.col("Description").str.to_lowercase().str.contains(text_input, strict=False)
                )
            )

        # Add option to filter results
        filter = st.radio(
            "Filter by",
            key="Filter results",
            options=result_df["File"].unique()

        )
        
        st.session_state.result_df = result_df

        st.write("Results for ", text_input, type_of, " There is ", len(result_df), " results")

        show_results = True



if show_results:

    result_df = st.session_state.result_df

    # st.dataframe(result_df)

    for i in range(len(result_df)):
        with st.container(border=True):
            st.subheader(f"Feature: {result_df["Feature"][i]}")
            st.write(f"File: {result_df["File"][i]}")
            st.write("Type: " + result_df["Type"][i])
            st.write(result_df["Description"][i])
            st.divider()

            
            how= result_df["Proccess"][i]


            if how == None:
                how = ["No information available"]
            elif r'/n' in how:
                how = how.split(r'/n') 
            else:
                how = [how]

            st.write("How we got it:")

            for j in range(len(how)):
                st.write(how[j])
                
            if result_df["Source Code Lines"][i] != None:
                st.write("Source Code Line: ", result_df["Source Code Lines"][i])

            page = result_df["Page"][i]

            pages_dicts = {
                "Extract Sleep": r"pages\5_😴_Extract_Sleep_Data.py",
                "Preprocess": r'pages/6 💓🚶‍♂️ Preprocessing.py',
                "Combine Step": r"pages\7_🤗_Combine_Step.py",
                "EDA Extraction": r"pages\10_⚡_EDA_Analysis.py",
                "HRV Analysis": r"pages\11_💞_HRV_Analysis.py",
                "Final File": r"pages\12_🙌_Final_File.py",
            }

            # page_link = pages_dicts[page]
            
            # st.page_link(page_link, label=f":green[Go to {result_df["Page"][i]} page]", icon="🔗")


