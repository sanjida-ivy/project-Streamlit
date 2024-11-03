import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page layout and title
st.set_page_config(layout="wide")
st.title("Battery Data Analytics")
st.subheader("Exploratory Data Analysis (EDA)")

# Load and display overview Excel data
@st.cache_data
def load_overview():
    df_overview = pd.read_excel('Inputdata/MeasurementData/Overview.xlsx')
    df_overview = df_overview.drop(['Unnamed: 13', 'Note'], axis=1)
    df_overview = df_overview.dropna()
    df_overview.rename(columns={'Unnamed: 8': 'SoC difference'}, inplace=True)
    return df_overview

# Load the overview data
df_overview = load_overview()

# Generate descriptions based on data types and unique values
column_descriptions = {}
for column in df_overview.columns:
    col_type = df_overview[column].dtype
    unique_values = df_overview[column].nunique()
    description = f"Type: {col_type}, Unique values: {unique_values}"
    column_descriptions[column] = description

# Select columns to display (set default to the first two columns)
default_columns = df_overview.columns.tolist()[:5]  # Change this to select your desired default columns
selected_columns = st.multiselect("Select columns to display", options=df_overview.columns.tolist(), default=df_overview.columns.tolist())

# Set a minimum height for both containers
min_height = "10px"  # Minimum height for responsive design

# Show the selected columns in the DataFrame and descriptions side by side
if selected_columns:
    col1, col2 = st.columns([3, 2])  # Create two columns with a ratio of 3:1

    with col1:
        st.write("### Selected Data")
        # Responsive container for the DataFrame
        st.markdown(f"<div style='min-height: {min_height}; height: auto; overflow: auto;'>", unsafe_allow_html=True)
        st.dataframe(df_overview[selected_columns], use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.write("### Summary Statistics")
        # Responsive container for the descriptions
        st.markdown(f"<div style='min-height: {min_height}; height: auto; overflow: auto;'>", unsafe_allow_html=True)
        
        # Summary Statistics
        # Convert selected columns to numeric, coercing errors
        numeric_columns = df_overview[selected_columns].apply(pd.to_numeric, errors='coerce')

        summary_stats = df_overview[selected_columns].describe().T  # Transpose to make it easier to read
        summary_stats['mean'] = summary_stats['mean'].round(2)
        summary_stats['50%'] = summary_stats['50%'].round(2)  # 50% is the median
        summary_stats['min'] = summary_stats['min'].round(2)
        summary_stats['max'] = summary_stats['max'].round(2)
        summary_stats['std'] = summary_stats['std'].round(2)

        # Select the relevant columns for display
        summary_stats_display = summary_stats[['mean', '50%', 'min', 'max', 'std']]
        summary_stats_display.columns = ['Mean', 'Median', 'Min', 'Max', 'Std Dev']  # Rename for clarity

        # Display summary statistics
        st.dataframe(summary_stats_display)

    # Select only numerical columns for visualization
    numerical_columns = [col for col in selected_columns if pd.api.types.is_numeric_dtype(df_overview[col])]

    # Check if there are any numerical columns to plot
    if numerical_columns:
        # Histograms and KDE Plots
        st.write("### Histograms and KDE Plots")
        num_columns = len(numerical_columns)
        plot_columns = st.columns(num_columns)  # Create as many columns as there are numerical columns

        for i, column in enumerate(numerical_columns):
            with plot_columns[i]:
                fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the size as needed
                
                # Create histogram and KDE
                sns.histplot(df_overview[column], bins=30, kde=True, stat='density', ax=ax)
                ax.set_title(f"Histogram and KDE for {column}")
                ax.set_xlabel(column)
                ax.set_ylabel('Density')

                # Display the plot
                st.pyplot(fig)

        # Correlation Matrix and Pairwise Scatter Plots
        if len(numerical_columns) > 0:
            st.write("### Correlation Matrix and Pairwise Scatter Plots")
            
            # Create two columns for the correlation matrix and pairwise scatter plots
            col_corr, col_scatter = st.columns(2)  # Two columns

            # Correlation Matrix
            with col_corr:
                correlation_matrix = df_overview[numerical_columns].corr()
                plt.figure(figsize=(10, 6))
                sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
                plt.title("Correlation Matrix")
                st.pyplot(plt)

            # Pairwise Scatter Plots
            with col_scatter:
                if len(numerical_columns) <= 10:  # Limit pair plots to a reasonable number of columns
                    pair_plot_fig = sns.pairplot(df_overview[numerical_columns])
                    st.pyplot(pair_plot_fig)
                else:
                    st.write("### Pairwise scatter plots are only displayed for up to 10 selected columns.")
    else:
        st.write("### No numerical columns selected for visualization.")

else:
    st.write("### No columns selected.")

# Descriptive Statistics
st.header("Descriptive Statistics")
st.write("Summary Statistics Table: Display mean, median, min, max, and standard deviation. Interactive Summary: User-selectable features for analysis.")

st.header("Data Distributions")
st.write("Histograms: For each variable. KDE Plots: Kernel density estimation for smooth distributions.")
st.header("Correlations and Relationships")
st.write("Correlation Matrix: Visual heatmap of correlations. Scatter Plots: Pairwise scatter plots to show relationships.")

st.header("Anomaly Detection")
st.write("Outlier Visualization: Highlight outliers in data plots. Statistical Methods: Techniques for detecting anomalies.")

st.header("Data Quality Checks")
st.write("Missing Values Analysis: Display counts and methods for handling. Duplicates Identification: Check for and handle duplicate entries. Consistency Checks: Ensure data formats and types are correct.")
