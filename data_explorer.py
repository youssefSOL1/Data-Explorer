import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Simple data explorer')

uploaded_file = st.file_uploader("Upload a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    

    st.subheader('Data Summary')
    st.write(df.describe())
    st.write('Shape of the data:', df.shape)
    st.write('Data Types:', df.dtypes)
    

    st.subheader('Data Visualization')
    
    plot_type = st.selectbox("Choose Plot Type",["Histogram","Scatter Plot","Correlation Heatmap"])
    
    if plot_type == "Histogram":
        column = st.selectbox("Select column",df.columns)
        st.write(f'Histogram of {column}')
        fig, ax = plt.subplots()
        df[column].plot(kind='hist',ax=ax)
        st.pyplot(fig)
        
    elif plot_type == "Scatter Plot":
        x_column =st.selectbox("Select X column",df.columns)
        y_column =st.selectbox("Select Y column",df.columns)
        st.write(f'Scatter Plot between {x_column} and {y_column}')
        fig, ax = plt.subplots()
        df.plot(kind='scatter',x=x_column,y=y_column,ax=ax)
        st.pyplot(fig)
        
    elif plot_type == "Correlation Heatmap":
        st.write('Correlation Heatmap')
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax=ax, annot=True, cmap='coolwarm')
        st.pyplot(fig)
        
        
        
    st.subheader('Filter and Sort Data')

    filter_column = st.selectbox("Select Column to Filter", df.columns)
    filter_value = st.text_input(f"Filter {filter_column} by")
    
    if filter_value:
        filtered_df = df[df[filter_column].astype(str).str.contains(filter_value)]
        st.write(filtered_df)
    
    sort_column = st.selectbox("Select Column to Sort", df.columns)
    sort_order = st.radio("Sort Order", ("Ascending", "Descending"))
    sorted_df = df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))
    st.write(sorted_df)

