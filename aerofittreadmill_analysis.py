# import libraries
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Setting the page configuration of streamlit Dashboard
st.set_page_config(page_title = "Aerofit Treadmill Analysis",layout = "wide")
st.title("Aerofit Treadmill Data Analysis Dashboard")

# Upload the dataset
uploaded_file = st.file_uploader("Please upload your dataset", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Basic Data Analysis
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    # Shape of the Dataset
    st.subheader("Shape of the dataset: ")
    st.write("Number of rows and columns in the dataset are :  ",df.shape)
    st.write("Column names of my dataset are :  ",df.columns.tolist())
    
    # Radio buttons
    st.subheader("Statistics of the Dataset")
    selected_option = st.radio(
        "Select what you want to display:",
        ("None", "Dataset info", "Missing Values", "Statistical Summary")
    )
    if selected_option == "Dataset Information":
        st.subheader("Dataset Information") 
    elif selected_option == "Missing values":
        st.subheader("Missing Values")
        st.write(df.isna().sum(axis=0))   
    elif selected_option == "Statistical summary":
        st.subheader("Statistical summary")
        st.write(df.describe())
    
    # Create few Checkboxes
    st.subheader("Statistics of the Dataset")
    data_info = st.checkbox("Show dataset information")
    missing_value = st.checkbox("show missing values")
    statistics = st.checkbox("Show the Statistical Summary of the dataset")
    
    if data_info :
        st.write("The Data types in this dataset are :  ",df.info())
    if missing_value :
        st.write("Missing values of the Dataset are : ",df.isna().sum(axis = 0))
    if statistics :
        st.write("Dataset statistics are : ",df.describe())
     
     
    # Visual Analysis of our Dataset
    # Column Selector 
    numeric_cols = df.select_dtypes(include = ["int64","float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include = ["object"]).columns.tolist()   
    st.write(numeric_cols)
    st.write(categorical_cols)

    # Uni Variate analysis
    # count plot
    st.subheader("Count Plot")
    selected_cols = st.selectbox("Select a numeric columns : ",numeric_cols)
    fig,ax = plt.subplots()
    sns.countplot(x = df[selected_cols],ax = ax)
    st.pyplot(fig)
    
    #   # count plot
    # st.subheader("Count Plot")
    # selected_cols = st.selectbox("Select a categorical columns : ",categorical_cols)
    # fig,ax = plt.subplots()
    # sns.countplot(x = df[cat_cols],ax = ax)
    # st.pyplot(fig)

    # Box plot for numeric columns
    st.subheader("box plot for checking the outliers")
    box_cols = st.selectbox("Select a numeric column : ",numeric_cols)
    fig,ax = plt.subplots()
    sns.boxplot(x = df[box_cols],ax = ax)
    st.pyplot(fig)

#    # Histogram plot for numeric columns
#     st.subheader("Hist plot")
#     hist_col = st.selectbox("Select a numeric column : ", numeric_cols)
#     fig, ax = plt.subplots()
#     sns.histplot(df[hist_col], kde=True, ax=ax, bins=30)
#     ax.set_title(f"Distribution of {hist_col}")
#     st.pyplot(fig)
    
    # Bivariate Analysis
    st.subheader("Bi-Variate Analysis of our Dataset : Categorical Vs Numerical")
    num_cols = st.selectbox("Select a numeric column :  ",numeric_cols,key = 'num1')
    category_cols = st.selectbox("Select a Categorical Column : ",categorical_cols,key ="cat1")
    fig,ax = plt.subplots()
    sns.boxplot(x = df[num_cols],y = df[category_cols],ax = ax)
    st.pyplot(fig)
    
    # scatter plot
    st.subheader("Bi-Variate Scatter Plot: Numeric vs Numeric")
    x_col = st.selectbox("Select X-axis numeric column:", numeric_cols, key="xaxis")
    y_col = st.selectbox("Select Y-axis numeric column:", numeric_cols, key="yaxis")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f"{y_col} vs {x_col}")
    st.pyplot(fig)
    
    # Multi - Variate Analysis
    # Heatmap of our dataset to check the co-relation
    st.subheader("Co-relation Heatmap")
    fig,ax = plt.subplots(figsize = (10,6))
    sns.heatmap(df[numeric_cols].corr(),annot = True,cmap = "magma",ax = ax)
    st.pyplot(fig)


else:
    st.write("please upload the Dataset first for the exploratory data analysis")    