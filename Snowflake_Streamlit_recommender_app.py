# Import python packages
import streamlit as st
import base64
import pandas as pd
from snowflake.snowpark.context import get_active_session
	
# Keeping pandas from truncating long strings
pd.set_option('display.max_colwidth', 1000)

# Get the current credentials
session = get_active_session()

# access underlying snowflake tables
# let participants define this?-----------
clothing_link_df = session.table("clothing_link").to_pandas()
clothing_links = clothing_link_df['LINKS']

# Write directly to the app
st.title("Clothing Recommender")

# Add some cosmetic headers
st.caption("Using Azure OpenAI with Snowflake to recommend wardrobes")

default_prompt = 'Please review the provided image and recommend the top three links from the provided list that this person would most likely want to wear. Display the complete url for the link in your response as it is provided in the request.'
with st.expander("Adjust system prompt"):
    system = st.text_area("System instructions", value=default_prompt).replace("'","")
st.markdown('------') 

# widget for image filter
selected_image = st.selectbox(
    'Select an image',
     session.sql("SELECT RELATIVE_PATH FROM DIRECTORY(@image_stage)"))

image_string = session.sql(f"""select GET_PRESIGNED_URL(@image_stage, '{selected_image}')""").collect()[0][0]
st.image(image_string)

# Use the job description to write the job to a table and run the function against it:
if(st.button('Ask ChatGPT')):
    result = session.sql(f"""SELECT chatgpt_image('{system}','{clothing_links}','{image_string}')""").collect()
    st.header('Answer')
    st.write(result[0][0].replace('"','')) 