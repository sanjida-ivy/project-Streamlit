import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the page layout
st.set_page_config(layout="wide")

# Sidebar menu
st.sidebar.title("Menu")
menu_option = st.sidebar.selectbox("Choose a section", ["Overview", "Data", "Analysis", "Settings"])

# Day/Night Mode Toggle
theme_mode = st.sidebar.radio("Select Theme Mode", ["Day Mode", "Night Mode"])

# Set theme colors
if theme_mode == "Day Mode":
    background_color = "#f4f4f4"
    text_color = "black"
    chart_background = "white"
else:
    background_color = "#333333"
    text_color = "white"
    chart_background = "#333333"

# Apply consistent styling for all containers
st.markdown(f"""
    <style>
        .container-box {{
            background-color: {background_color};
            padding: 15px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            color: {text_color};
            margin-bottom: 15px;
        }}
    </style>
""", unsafe_allow_html=True)

# Main dashboard area
st.title("Dashboard")

# Sample data for visualization and table
data = pd.DataFrame({
    'Metric': ['Metric A', 'Metric B', 'Metric C', 'Metric D'],
    'Value': [np.random.randint(100, 500) for _ in range(4)]
})

chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['Value 1', 'Value 2']
)

# Row 1: Display summary stats in 4 columns with consistent styling
#st.subheader("Summary Statistics")
col1, col2, col3, col4 = st.columns(4)
for col, (metric, value) in zip([col1, col2, col3, col4], data.values):
    with col:
        with st.container():
            st.markdown(f"<div class='container-box'><h4 style='color:{text_color};'>{metric}</h4><p style='font-size:24px;'><strong>{value}</strong></p></div>", unsafe_allow_html=True)

# Row 2: Display a chart in the first column and a data table in the second column
#st.subheader("Data Analysis")
col5, col6 = st.columns(2)

# First column: Line or Bar Chart without HTML containers for better alignment
with col5:
    with st.container():
        #st.markdown(f"<h4 style='color:{text_color};'>Chart</h4>", unsafe_allow_html=True)
        chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart"])
        fig, ax = plt.subplots(facecolor=chart_background)
        ax.set_facecolor(chart_background)
        
        # Set chart color styling
        ax.spines['bottom'].set_color(text_color)
        ax.spines['left'].set_color(text_color)
        ax.tick_params(axis='x', colors=text_color)
        ax.tick_params(axis='y', colors=text_color)
        
        if chart_type == "Line Chart":
            ax.plot(chart_data.index, chart_data['Value 1'], label="Value 1", color="tab:blue")
            ax.plot(chart_data.index, chart_data['Value 2'], label="Value 2", color="tab:orange")
        else:
            ax.bar(chart_data.index, chart_data['Value 1'], label="Value 1", color="tab:blue")
            ax.bar(chart_data.index, chart_data['Value 2'], label="Value 2", color="tab:orange")
        ax.legend()
        st.pyplot(fig)

# Second column: Data Table in container
with col6:
    with st.container():
        st.markdown(f"<p style='color:{text_color};'>Chart</p>", unsafe_allow_html=True)
        styled_data = chart_data.style.set_properties(**{
            'background-color': background_color,
            'color': text_color
        })

        st.write(styled_data)
        

# Row 3: Two charts side by side
#st.subheader("Additional Insights")
col7, col8 = st.columns(2)

# First chart in Row 3
with col7:
    with st.container():
        #st.markdown(f"<div class='container-box'><h4>{metric}</h4><p style='font-size:24px;'><strong>{value}</strong></p></div>", unsafe_allow_html=True)
        fig2, ax2 = plt.subplots(facecolor=chart_background)
        ax2.set_facecolor(chart_background)
        ax2.plot(chart_data.index, chart_data['Value 2'], color="tab:orange")
        ax2.spines['bottom'].set_color(text_color)
        ax2.spines['left'].set_color(text_color)
        ax2.tick_params(axis='x', colors=text_color)
        ax2.tick_params(axis='y', colors=text_color)
        ax2.set_title(label="ReLU function graph",
          fontsize=12,
          color=text_color, pad='20.0', loc='left')
        st.pyplot(fig2)

# Second chart in Row 3
with col8:
    with st.container():
        #st.markdown(f"<div class='container-box'><h4>{metric}</h4><p style='font-size:24px;'><strong>{value}</strong></p></div>", unsafe_allow_html=True)
        fig2, ax2 = plt.subplots(facecolor=chart_background)
        ax2.set_facecolor(chart_background)
        ax2.plot(chart_data.index, chart_data['Value 2'], color="tab:orange")
        ax2.spines['bottom'].set_color(text_color)
        ax2.spines['left'].set_color(text_color)
        ax2.tick_params(axis='x', colors=text_color)
        ax2.tick_params(axis='y', colors=text_color)
        ax2.set_title(label="ReLU function graph",
          fontsize=12,
          color=text_color, pad='20.0', loc='left')
        st.pyplot(fig2)


