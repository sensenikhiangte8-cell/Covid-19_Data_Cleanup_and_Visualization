import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="COVID-19 Analytics Dashboard",
    page_icon="🦠",
    layout="wide"
)
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #F4F6F9;
    }

    /* Main header */
    h1 {
        color: #1F2A44;
        font-weight: 700;
    }

    /* Subheaders */
    h2, h3, h4 {
        color: #2C3E50;
        font-weight: 600;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #1F2A44;
        color: white;
    }

    section[data-testid="stSidebar"] .css-1v0mbdj {
        color: white;
    }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    /* Dataframe styling */
    .stDataFrame {
        background-color: white;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================
st.title("🦠 COVID-19 Analytics Dashboard")
st.markdown("Interactive Data Cleaning & Visualization")
st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_data():
    df = pd.read_csv("day_wise.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df.columns = df.columns.str.strip().str.title()
    df = df.fillna(0)
    df = df.drop_duplicates()
    return df

df = load_data()

# =====================================================
# SIDEBAR FILTERS
# =====================================================
st.sidebar.header("🎛 Dashboard Filters")

start_date = pd.to_datetime(
    st.sidebar.date_input("Start Date", df["Date"].min().date())
)

end_date = pd.to_datetime(
    st.sidebar.date_input("End Date", df["Date"].max().date())
)

df_filtered = df[
    (df["Date"] >= start_date) &
    (df["Date"] <= end_date)
].copy()

# =====================================================
# METRIC CARDS
# =====================================================
st.subheader("📊 Key Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Confirmed",
    f"{int(df_filtered['Confirmed'].max()):,}"
)

col2.metric(
    "Total Deaths",
    f"{int(df_filtered['Deaths'].max()):,}"
)

col3.metric(
    "Total Recovered",
    f"{int(df_filtered['Recovered'].max()):,}"
)

st.markdown("---")

# =====================================================
# GLOBAL TRENDS
# =====================================================
st.subheader("📈 Global COVID-19 Trends")

fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df_filtered["Date"], df_filtered["Confirmed"], label="Confirmed")
ax1.plot(df_filtered["Date"], df_filtered["Deaths"], label="Deaths")
ax1.plot(df_filtered["Date"], df_filtered["Recovered"], label="Recovered")
ax1.legend()
ax1.grid(True, alpha=0.3)

st.pyplot(fig1)

st.markdown("---")

# =====================================================
# DAILY NEW CONFIRMED CASES
# =====================================================
st.subheader("📉 Daily New Confirmed Cases")

df_filtered["New_Confirmed"] = df_filtered["Confirmed"].diff()

fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.plot(df_filtered["Date"], df_filtered["New_Confirmed"])
ax2.grid(True, alpha=0.3)

st.pyplot(fig2)

st.markdown("---")

# =====================================================
# CORRELATION HEATMAP
# =====================================================
st.subheader("🔥 Correlation Heatmap")

corr = df_filtered[["Confirmed", "Deaths", "Recovered"]].corr()

fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)

st.pyplot(fig3)

st.markdown("---")

# =====================================================
# DATA PREVIEW
# =====================================================
st.subheader("📄 Cleaned Dataset Preview")
st.dataframe(df_filtered.tail(10), use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Built with Streamlit • Data Science Mini Project • 2026"
    "</p>",
    unsafe_allow_html=True
)
