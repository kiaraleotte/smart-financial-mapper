import streamlit as st
import pandas as pd

st.title("Smart Financial Mapper")
st.write("Version 1 - File Upload")

source_file = st.file_uploader("Upload Source CSV", type=["csv"])
dest_file = st.file_uploader("Upload Destination CSV", type=["csv"])

if source_file is not None and dest_file is not None:
    st.success("Both files uploaded successfully!")
elif source_file is not None or dest_file is not None:
    st.info("Please upload both the source and destination CSV files.")