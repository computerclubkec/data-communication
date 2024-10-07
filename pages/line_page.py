"""
This Streamlit application provides an interface for line encoding and decoding of signal bits.
Modules:
    streamlit: Provides the web interface.
    signals: Contains the Signals class for handling signal operations.
    line: Contains various line encoding and decoding functions.
Streamlit Widgets:
    st.text_input: Input field for entering signal bits.
    st.selectbox: Dropdown for selecting line encoding method.
    st.selectbox: Dropdown for selecting encoding or decoding.
Workflow:
    1. User inputs signal bits.
    2. User selects a line encoding method.
    3. User selects whether to encode or decode the signal.
    4. The corresponding encoding/decoding function is called based on user selection.
    5. The original and processed signals are displayed using matplotlib.
"""
import streamlit as st
from signals import Signals
from line import bipolar_nrz, bipolar_rz, manchester, diff_manchester, polar_nrz, polar_rz, unipolar_nrz, unipolar_rz, nrz_invert, nrz_level

st.set_page_config(page_title="Line Encoding and Decoding", page_icon="📈")

signal_input = st.text_input("Enter Signal Bits", placeholder="Eg. 100101101")
option = st.selectbox("Select Line Encoding Method",
                       ("---", "Bipolar NRZ", "Bipolar RZ",
                       "Diff Manchester", "Manchester",
                       "NRZ Invert", "NRZ Level",
                       "Polar NRZ", "Polar RZ",
                       "Unipolar NRZ", "Unipolar RZ"))

enc_or_dec = st.selectbox("Encoding or Decoding the signal", ("Encoding", "Decoding"))

if signal_input and option != "---" and enc_or_dec:
    signal = Signals(signal_input)
    original_signal = signal.display(show=False)
    line_functions = {
        "Bipolar NRZ": bipolar_nrz,
        "Bipolar RZ": bipolar_rz,
        "Diff Manchester": diff_manchester,
        "Manchester": manchester,
        "NRZ Invert": nrz_invert,
        "NRZ Level": nrz_level,
        "Polar NRZ": polar_nrz,
        "Polar RZ": polar_rz,
        "Unipolar NRZ": unipolar_nrz,
        "Unipolar RZ": unipolar_rz
    }

    sel_method = line_functions[option]


    METHOD_SUFFIX = "_encode" if enc_or_dec == "Encoding" else "_decode"
    method_name = option.lower().replace(" ","_") + METHOD_SUFFIX
    method_to_call = getattr(sel_method, method_name)
    method_to_call(signal)

    if sel_method and enc_or_dec:
        st.pyplot(original_signal)
        st.pyplot(signal.display(show=False))
