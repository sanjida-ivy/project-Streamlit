import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set Streamlit page layout and title
st.set_page_config(layout="wide")
st.title("Battery Data Analytics")

# Load and display overview Excel data
@st.cache_data
def load_overview():
    df_overview = pd.read_excel('Inputdata/MeasurementData/Overview.xlsx', encoding='utf-8')
    df_overview = df_overview.drop(['Unnamed: 13', 'Note'], axis=1)
    df_overview = df_overview.dropna()
    df_overview.rename(columns={'Unnamed: 8': 'SoC difference'}, inplace=True)
    return df_overview

st.write("### Overview Data")
df_overview = load_overview()
st.dataframe(df_overview)

# Load and display combined trip data
@st.cache_data
def load_combined_trip():
    df_combinedTrip = pd.read_csv('Inputdata/MeasurementData/TripA01.csv', encoding='utf-8')
    return df_combinedTrip

st.write("### All Trip Data")
df_combinedTrip = load_combined_trip()
st.dataframe(df_combinedTrip.sample(n=10))

# Load and process df_master (make sure to define how to load it)
@st.cache_data
def load_master():
    df_master = pd.read_csv('Inputdata/MeasurementData/TripA01.csv', encoding='utf-8')  # Example file path
    df_master = df_master.iloc[:, :-2]  # Remove last 2 columns
    return df_master

st.write("### Master Data")
df_master = load_master()
st.dataframe(df_master)

# Print the remaining column names
st.write("### Remaining Columns in Master Data")
remaining_columns = list(df_master.columns.values)
st.write(remaining_columns)  # Display the column names in Streamlit

# Define the plotting function (if not already defined)
def plot_dataframe_subplots(df, nrows, ncols, figsize):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for i, column in enumerate(df.columns):
        ax = axes[i // ncols, i % ncols]
        df[column].plot(ax=ax, title=column)
        ax.set_xlabel('Index')
        ax.set_ylabel(column)
    plt.tight_layout()
    st.pyplot(fig)  # Use Streamlit to display the plot
    
# Plot results of all trips
st.write("### Trip Data Plots")
plot_dataframe_subplots(df_master, nrows=12, ncols=4, figsize=(30, 48))