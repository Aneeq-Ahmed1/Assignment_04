import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    # Plotting
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter by", columns)
    unique_values = df[selected_columns].unique().tolist()
    selected_values = st.selectbox("Select values to filter by", unique_values)

    filtered_df = df[df[selected_columns] == (selected_values)]
    st.write(filtered_df) 

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Please upload a CSV file.")