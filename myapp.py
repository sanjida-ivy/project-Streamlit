import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)
eda = st.Page("analysis/eda.py", title="EDA", icon=":material/insights:")
data_preprocessing = st.Page("analysis/data_preprocessing.py", title="Data Preprocessing", icon=":material/build:")
feature_engineering = st.Page("analysis/feature_engineering.py", title="Feature Engineering", icon=":material/science:")
statistical_analysis = st.Page("analysis/statistical_analysis.py", title="Statistical Analysis", icon=":material/bar_chart:")
trend_cycle_analysis = st.Page("analysis/trend_cycle_analysis.py", title="Trend and Cycle Analysis", icon=":material/trending_up:")
time_series_analysis = st.Page("analysis/time_series_analysis.py", title="Time-Series Analysis", icon=":material/show_chart:")
visualization = st.Page("analysis/visualization.py", title="Visualization", icon=":material/pie_chart:")
predictive_modeling = st.Page("analysis/predictive_modeling.py", title="Predictive Modeling", icon=":material/insights:")


search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
            "Analysis": [
                eda, 
                data_preprocessing, 
                feature_engineering, 
                statistical_analysis,
                trend_cycle_analysis,
                time_series_analysis,
                visualization,
                predictive_modeling,
            ],
        }
    )
    
else:
    pg = st.navigation([login_page])

pg.run()