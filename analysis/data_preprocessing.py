import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data for demonstration purposes
# Replace this with your actual dataset
@st.cache
def load_data():
    # For example, using the Iris dataset
    data = sns.load_dataset("iris")
    return data

# Load dataset
df = load_data()

st.title("Data Preprocessing")

# Descriptive Statistics
st.header("Data Cleaning")
st.write("Missing Value Imputation: Strategies for filling in missing data.Outlier Removal Techniques: Approaches to deal with outliers.Data Formatting: Standardizing data formats (e.g., date formats).")

st.header("Data Standardization")
st.write("Normalization: Min-max scaling methods.Z-score Standardization: Standardizing to have mean 0 and std dev 1.")


