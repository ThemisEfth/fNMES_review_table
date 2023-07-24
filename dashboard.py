# Created by Themis Efthimiou in July 2023
# This is part of a paper currently hosted on PsyArchiv
    # Efthimiou, T. N., Hernandez, M. P., Elsenaar, A., Mehu, M., & Korb, S. (2022).
    # Application of facial Neuromuscular Electrical Stimulation (fNMES) in
    # psychophysiological research–systematic review and practical recommendations.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
data = pd.read_csv('Data/table_for_db.csv')

# Streamlit app
def main():
    st.title('Results from a systematic review of 134 studies utilising fNMES')

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

    # Create a histogram using Matplotlib
    st.subheader('Histogram of electrode surface area cm2')
    fig, ax = plt.subplots()
    ax.hist(data['Elec surface (cm2)'], bins=10, edgecolor='black')
    # Add x and y-axis labels
    ax.set_xlabel('Electrode Surface Area (cm2)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Create a histogram using Matplotlib
    st.subheader('Histogram of Pulse Widths')
    fig, ax = plt.subplots()
    ax.hist(data['Phase pulse Width (usec)'], bins=10, edgecolor='black')
    # Add x and y-axis labels
    ax.set_xlabel('Pulse Width (usec)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Display filtered data in a table
    st.subheader('Filtered Data Table')
    st.table(filtered_data)

if __name__ == '__main__':
    main()
