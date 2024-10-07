"""
This module creates the homepage for the Data Communication Tools web application.
It includes a brief introduction and provides access to different tools related to
line encoding, channel encoding, and source encoding, developed by Kantipur Engineering
College Computer Club.
"""

import streamlit as st

# Setting the page configuration
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# Title of the page
st.title("🌐 Data Communication Tools")

# Markdown section with introduction and description
st.markdown(
    '''
    Welcome to the Data Communication Tools, a comprehensive collection of powerful tools 
    designed to simplify and enhance your data communication processes, developed by 
    [Kantipur Engineering College Computer Club](https://github.com/computerclubkec). 
    Whether you're working on source encoding, channel encoding, or line encoding, we've got you covered.

    Our curated set of utilities helps you encode, transmit, and decode data with reliability and efficiency.
    Dive into the world of data communication and explore our range of tools, each crafted to meet the demands 
    of modern technology. Join us in making data transmission seamless and robust. Contribute, innovate, and 
    collaborate with our growing community!
    '''
)

# Creating columns for layout
col1, col2, col3 = st.columns(3)

# Column 1 content: Line Encoding and Decoding
with col1:
    with st.container():
        st.image("https://www.eeweb.com/wp-content/uploads/articles-quizzes-line-coding-1422602410.png")
        if st.button("Line Encoding and Decoding"):
            st.switch_page("pages/line_page.py")

# Column 2 content: Channel Encoding and Decoding
with col2:
    with st.container():
        st.image("https://media.geeksforgeeks.org/wp-content/uploads/20200122012046/edited2.png")
        if st.button("Channel Encoding and Decoding"):
            st.switch_page("pages/channel_page.py")

# Column 3 content: Source Encoding and Decoding
with col3:
    with st.container():
        st.image("https://media.springernature.com/lw685/springer-static/image/"
                 "chp%3A10.1007%2F978-981-19-0920-7_3/MediaObjects/525386_1_En_3_Fig2_HTML.png")
        if st.button("Source Encoding and Decoding"):
            st.switch_page("pages/source_page.py")
