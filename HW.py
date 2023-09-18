pip install plotly
pip install pandas
import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="Interactive Visualizations", layout="wide")

# Load your data
df = pd.read_csv("C:/Users/abdal/Downloads/archive (3)/Original_raw_NoIndex_YesHeader-.csv")

# Define your visualizations
def scatter_plot():
    st.title('Engine Capacity vs. Horsepower')
    Scatter_Plot = px.scatter(df, x='Engine Capacity (liters)', y='Horsepower (bhp)',
                               title='Engine Capacity vs. Horsepower', color='Fuel Type', hover_name='name')
    Scatter_Plot.update_traces(marker=dict(size=8), selector=dict(mode='markers+text'))
    Scatter_Plot.update_layout(showlegend=True)
    st.plotly_chart(Scatter_Plot)

def box_plot():
    st.title('Fuel Type vs. Fuel Economy')
    Box_plot = px.box(df, x='Fuel Type', y='Fuel Economy (L/100 Km)',
                       title='Fuel Type vs. Fuel Economy', color='Fuel Type')
    Box_plot.update_layout(xaxis_title='Fuel Type', yaxis_title='Fuel Economy (L/100 Km)')
    st.plotly_chart(Box_plot)

def bar_chart():
    st.title('Drive Type Distribution')
    Bar_chart = px.bar(df['Drive Type'].value_counts().reset_index(), x='index', y='Drive Type',
                       title='Drive Type Distribution', color='index')
    Bar_chart.update_layout(xaxis_title='Drive Type', yaxis_title='Count')
    Bar_chart.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                            marker_line_width=1.5, opacity=0.7)
    st.plotly_chart(Bar_chart)

# Create a sidebar with interactive features
st.sidebar.title("Interactive Features")

# Interactive feature 1: Toggle visualizations
visualization_option = st.sidebar.selectbox("Select Visualization", ["Scatter Plot", "Box Plot", "Bar Chart"])

if visualization_option == "Scatter Plot":
    scatter_plot()
elif visualization_option == "Box Plot":
    box_plot()
elif visualization_option == "Bar Chart":
    bar_chart()

# Interactive feature 2: Show data table
if st.sidebar.checkbox("Show Data Table"):
    st.title("Data Table")
    st.write(df)

# Interactive feature 3: Show summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.title("Summary Statistics")
    st.write(df.describe())
