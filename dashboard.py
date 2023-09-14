# Created by Themis Efthimiou in July 2023
# This is part of a paper currently hosted on PsyArchiv
    # Efthimiou, T. N., Hernandez, M. P., Elsenaar, A., Mehu, M., & Korb, S. (2022).
    # Application of facial Neuromuscular Electrical Stimulation (fNMES) in
    # psychophysiological research–systematic review and practical recommendations.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/table_for_DB.csv")

# Streamlit app
def main():
    st.title('Systematic Review - Efthimiou et al. 2023')

    # Add data exploration widgets here
    # e.g., filters, sliders, etc.

    # Display data in a table
    st.subheader('Data Table')
    st.dataframe(data)

    # Filter by goal
    goal = data['Goal'].unique().tolist()
    goal_filter = st.sidebar.multiselect('Filter by intended goal', goal, default=[])

    # Filter by pulse type
    pulsetype = data['Pulse type'].unique().tolist()
    pulsetype_filter = st.sidebar.multiselect('Filter by pulse type', pulsetype, default=[])

    # Filter by Site
    site = data['Stimulation site'].unique().tolist()
    site_filter = st.sidebar.multiselect('Filter by stimulation site', site, default=[])

    # Filter by Waveform
    waveform = data['Waveform'].unique().tolist()
    waveform_filter = st.sidebar.multiselect('Filter by pulse waveform', waveform, default=[])

    # Apply filters
    filtered_data = data.copy()
    if goal_filter:
        filtered_data = filtered_data[filtered_data['Goal'].isin(goal_filter)]
    if site_filter:
        filtered_data = filtered_data[filtered_data['Stimulation site'].isin(site_filter)]
    if waveform_filter:
        filtered_data = filtered_data[filtered_data['Waveform'].isin(waveform_filter)]
    if pulsetype_filter:
        filtered_data = filtered_data[filtered_data['Pulse Type'].isin(pulsetype_filter)]

    # Create visualizations using matplotlib or other libraries
    st.subheader('Data Visualisation')

if __name__ == '__main__':
    main()
