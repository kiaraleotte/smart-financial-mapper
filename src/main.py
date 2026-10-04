import streamlit as st
import pandas as pd

st.title("Smart Financial Mapper")
st.write("Version 1 - File Upload")

# --- Upload source and dest file ---
source_file = st.file_uploader("Upload Source CSV", type=["csv"])
dest_file = st.file_uploader("Upload Destination CSV", type=["csv"])

# --- Validate source and dest file ---
if source_file is not None and dest_file is not None:
    st.success("Both files uploaded successfully!")
elif source_file is not None or dest_file is not None:
    st.error("Please upload both the source and destination CSV files.")

if source_file.size == 0:
    st.error("The source file is empty (0 bytes). Please upload a file with data.")
    
elif dest_file.size == 0:
    st.error("The destination file is empty (0 bytes). Please upload a file with data.")

else:
    try:
        source_df = pd.read_csv(source_file)
        dest_df = pd.read_csv(dest_file)
    except pd.errors.ParserError:
        st.error("One of the uploaded files could not be read as a valid CSV.")

