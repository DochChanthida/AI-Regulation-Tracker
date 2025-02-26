import streamlit as st
import pandas as pd

# Sample AI regulations data
data = {
    "Region": ["ASEAN", "EU", "U.S.", "China", "Singapore", "UK"],
    "Regulation": [
        "ASEAN AI Guide 2024",
        "EU AI Act",
        "NIST AI Risk Management Framework",
        "China AI Ethics Guidelines",
        "Singapore AI Governance Framework",
        "UK AI Transparency Guidelines"
    ],
    "Status": ["Adopted", "In Review", "Finalized", "Draft", "Implemented", "Proposed"],
    "Publication Date": ["2024-02-01", "2023-12-15", "2024-01-20", "2023-11-10", "2024-02-05", "2023-10-30"],
    "Key Focus": [
        "AI governance best practices",
        "Risk-based compliance & enforcement",
        "AI risk management for industry",
        "Ethical AI principles and compliance",
        "AI ethics & compliance in business",
        "Transparency and accountability in AI"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.title("AI Regulation Tracking Dashboard")

# Filters
region_filter = st.selectbox("Select Region:", ["All"] + list(df["Region"].unique()))
status_filter = st.selectbox("Select Status:", ["All"] + list(df["Status"].unique()))
search_query = st.text_input("Search Regulation:", "")

# Filtering Data
def filter_data():
    filtered_df = df.copy()
    if region_filter != "All":
        filtered_df = filtered_df[filtered_df["Region"] == region_filter]
    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status_filter]
    if search_query:
        filtered_df = filtered_df[filtered_df["Regulation"].str.contains(search_query, case=False, na=False)]
    return filtered_df

filtered_df = filter_data()

# Display Data
st.dataframe(filtered_df)
