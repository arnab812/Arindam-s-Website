import streamlit as st
import pandas as pd

# Data for the table
data = {
    "ID": ["001", "002", "003", "004", "005", "006", "007", "008"],
    "Name": ["Arnab", "Arindam", "Avi", "Jayanta", "Shreyan", "Gourav", "Soumya", "Sumit"],
    "Designation": ["Proprietor", "CEO", "Manager", "Asst. Manager", "Secretary", "Salesman", "Salesman", "Salesman"],
    "Salary": ["∞", "$10000", "$9000", "$8000", "$7000", "$6000", "$5000", "$4000"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table in Streamlit
st.title("Arindam")
st.write(Employee Info)
st.table(df)

# Add hyperlinks using HTML
st.markdown("""
<a href="https://www.google.co.in/" target="_blank">Google</a> <br>
<a href="https://www.pexels.com/photo/close-up-photography-of-brown-lion-33045/" target="_blank">Arindam</a> <br>
<a href="https://www.youtube.com/watch?v=2214fezAZh4" target="_blank">YouTube</a>
""", unsafe_allow_html=True)
