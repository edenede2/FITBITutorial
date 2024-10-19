import streamlit as st

st.title("Download fitbit data from API")

st.divider()

st.write(
    """
    In this step, we will guide you through the process of downloading your fitbit data from the fitbit API.
    
    We will cover the following topics:
    1. Get your Fitbit API token.
    2. Download your fitbit data.
    """
)

st.divider()

st.title("1. Get your Fitbit API token")

st.write(
    """
    To begin, you will need to log into your subject account (Google and fitbit emails are the same for this step) a fitbit developer account.

    This will allow you to register your application and get the necessary credentials to access the fitbit API for your subject account.
    
    Follow the steps below to set up your fitbit developer account.
    """
)

st.subheader("Instructions")




st.write(
    """
    1. Open a text file on your computer by right-clicking on your desktop and selecting 'New' -> 'Text Document'.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 204755.png"
)

st.write(
    """
    2. Add the following titles to the text file:

        - subjects client Ids: Your OAuth 2.0 Client ID, we will get this ids from the fitbit developer website in the next steps.
        - url: The url to get the token, we will get this url from the fitbit developer website in the next steps.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 210137.png"
)

st.write(
    """
    3. Save the text file in your 'Processed Data' 'Metadata' folder with the following name: 'api_tokens.txt'. We will use this file to store your fitbit API credentials.
    4. Go to the [fitbit developer website](https://dev.fitbit.com/) and open the 'Register an App' page.

    """
)

st.image(
    "pages/Screenshot 2024-10-11 203716.png"
)

st.write(
    """
    4. Log in with your fitbit account credentials.
    
        """
)

st.image(
    "pages/Screenshot 2024-10-11 190824.png"
)


st.write(
    """
    5. Select the 'REGISTER AN APP' tab.
        
            """
)

st.image(
    "pages/Screenshot 2024-10-11 203851.png"
)


st.write(
    """
    6. Fill the form with the following information:

        - Application Name: Your subject name (should not include the word fitbit and should include 12 characters or less).
        - Description: A brief description of your application (should not include the word fitbit and should include more then 20 characters).
        - Application Website URL: https://www.google.com.
        - Organization: University of Haifa.
        - Organization Website URL: https://www.google.com.
        - Terms of Service URL: https://www.google.com.
        - Privacy Policy URL: https://www.google.com.
        - OAuth 2.0 Application Type: Personal.
        - Redirect URLs: http://localhost
        - Default Access Type: Read-Only.
        - OAuth 2.0 Client ID: Your OAuth 2.0 Client ID.
        
        After filling the form, accept the terms and conditions and click on the 'Register' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 204431.png"
)

st.image(
    "pages/Screenshot 2024-10-11 204452.png"
)

st.write(
    """
    7. After registering your app, you will be redirected to the 'Manage My Apps' page. :red[DON'T CLOSE THIS PAGE]
    8. Open the 'api_tokens.txt' file that you created in step 2, write your subject id and copy the address below under the 'url' field.

        - https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23PTDL&redirect_uri=http://localhost&scope=activity%20heartrate%20location%20nutrition%20oxygen_saturation%20profile%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight&expires_in=31536000

    """
)

st.image(
    "pages/Screenshot 2024-10-11 210356.png"
)

st.write(
    """
    9. Copy the OAuth 2.0 Client ID that you received after registering your app and paste it in the 'api_tokens.txt' file under the 'subjects client Ids' field.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 210317.png"
)

st.image(
    "pages/Screenshot 2024-10-11 210356.png"
)


st.write(
    """
    10. Modify the url by replacing the 'client_id' value with your OAuth 2.0 Client ID. Make sure to copy it correctly.
    11. Save the 'api_tokens.txt' file.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 213543.png"
)

st.write(
    """
    12. Go back to the fitbit developer website and make sure you are still logged in.
    13. Copy the url from the 'api_tokens.txt' file and paste it in the browser's address bar and press 'Enter'.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 210653.png"
)

st.write(
    """
    14. You will be redirected to the verification page. 
    15. Make sure that the access for the requested data is allowed for a 1 year. If not make sure that the number of seconds is 31536000 in the end of your url.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 210913.png"
)


st.write(
    """
    16. Select 'Allow All' and click on the 'Allow' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 210936.png"
)


st.write(
    """
    17. You will be redirected to the 'localhost' page. :red[Ignore the page content]
    18. Copy the address from the browser's address bar to the 'api_tokens.txt' file under the 'redirect_uri' field.
    """

)

st.image(
    "pages/Screenshot 2024-10-11 211126.png"
)

st.image(
    "pages/Screenshot 2024-10-11 211204.png"
)

st.write(
    """
    19. Save the 'api_tokens.txt' file.
    20. Write a new title in the text file (if you don't have one) called 'access_token' and copy the access token from the redirect uri that you copied in the previous step. It should start after the 'access_token=' and end before the '&scope='.

    """
)

st.image(
    "pages/Screenshot 2024-10-11 211441.png"
)

st.image(
    "pages/Screenshot 2024-10-11 211604.png"
)

st.write(
    """
    21. Save the 'api_tokens.txt' file.
    22. We will use the tokens in the next step to download your fitbit data.
    """
)

st.divider()

st.title("2. Download your fitbit data")




st.write(
    """
    In this step, we will guide you through the process of downloading your fitbit data from the fitbit API.
    """
)

st.subheader("Instructions")



dependencies_container = st.container(border=True)

dependencies_container.markdown(
    """
    Before you run the download api script, ensure that you have the following:
    - The 'Experiment' folder with the necessary structure.
    - The 'Data' folder in the 'Experiment' folder (can be empty)
    - The 'Subjects Dates' file in the 'Metadata' folder with the subjects' dates.
    """
)

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
    2. Click on the 'download api' tab.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 211742.png"
)

st.write(
    """
    3. Load your project by selecting the project and clicking on the 'Load' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 211820.png"
)

st.write(
    """
    4. Review the table with the subjects that just loaded. This table shows the content of the 'subjects dates.csv' file that we created in the previous steps.
    5. Open the 'api_tokens.txt' file and copy the 'access_token' value to the 'token' field in the table.

    """
)

st.image(
    "pages/Screenshot 2024-10-11 212109.png"
)


st.write(
    """
    6. Select the subjects that you want to download the data for.
    7. Click on the 'Generate .zip file for selected subjects' button.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 212227.png"
)


st.write(
    """
    8. A black box will appear at the center of the screen. This box shows the progress of the download process.
    9. Wait until the download is complete, the box will disappear when the download is done.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 214117.png"
)

st.write(
    """
    10. You can find the downloaded zip files in the 'Data' folder in the 'Experiment' folder of your project.
    11. Open the Data folder and right-click on the zip file that you just downloaded and select 'Extract here'.
    12. Go to the 'set up' tab to continue with the next steps.
    """
)

st.image(
    "pages/Screenshot 2024-10-11 212657.png"
)