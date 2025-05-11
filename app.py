import streamlit as st
import pandas as pd
from parser import import_bank_statement

st.set_page_config(page_title="Bank Statement Importer", layout="centered")
st.title("🏦 Bank Statement Importer")
st.caption("Upload your bank CSV or Excel file for quick analysis and cleaning.")

# File uploader
uploaded_file = st.file_uploader("Upload bank statement (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

if uploaded_file:
    try:
        df = import_bank_statement(uploaded_file)
        st.success("✅ File imported successfully!")
        st.dataframe(df.head(20))

        # Offer cleaned data for download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name='cleaned_statement.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("Please upload a bank statement file to get started.")
