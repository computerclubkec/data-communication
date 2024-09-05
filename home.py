import streamlit as st



st.set_page_config(
    page_title = "Home",
    page_icon = "🏠",
)

st.title("🌐 Data Communication Tools")

st.markdown(
    '''
    Welcome to the Data Communication Tools, a comprehensive collection of powerful tools designed to simplify and enhance your data communication processes develoved by [Kantipur Engineering College Computer Club](https://github.com/computerclubkec). Whether you're working on source encoding, channel encoding, or line encoding, we've got you covered. Our curated set of utilities helps you encode, transmit, and decode data with reliability and efficiency.

    Dive into the world of data communication and explore our range of tools, each crafted to meet the demands of modern technology. Join us in making data transmission seamless and robust. Contribute, innovate, and collaborate with our growing community!
    '''
)

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True, height=
                      250):
        st.image("https://www.eeweb.com/wp-content/uploads/articles-quizzes-line-coding-1422602410.png")
        if st.button("Line Encoding and Decoding"):
            st.switch_page("pages/line.py")

with col2:
    with st.container(border=True, height=250):
        st.image("https://media.geeksforgeeks.org/wp-content/uploads/20200122012046/edited2.png")
        if st.button("Channel Encoding and Decoding"):
            st.switch_page("pages/line.py")

with col3:
    with st.container(border=True, height=250):
        st.image("https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-981-19-0920-7_3/MediaObjects/525386_1_En_3_Fig2_HTML.png")
        st.write("\n")
        st.write("\n")
        if st.button("Source Encoding and Decoding"):
            st.switch_page("pages/line.py")