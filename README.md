This repository contains a Streamlit application that leverages Azure OpenAI and Snowflake to recommend clothing based on provided images. The application allows users to select an image and receive recommendations for clothing links that are likely to be appealing based on the image content.
Features

    Image Selection: Choose an image from a predefined list stored in a Snowflake stage.
    Clothing Recommendation: Get clothing link recommendations using Azure OpenAI's capabilities.
    Customizable Prompt: Adjust the system prompt for the OpenAI model.
    Integration with Snowflake: Access clothing links and images stored in Snowflake.

Requirements

    Python 3.8 or higher
    Streamlit
    Pandas
    Snowflake Snowpark Python API
    Azure OpenAI API access

Using the App:

    Select an image from the dropdown menu.
    Optionally adjust the system prompt.
    Click on the "Ask ChatGPT" button to get clothing recommendations.
    View the recommended clothing links displayed in the app.
