#------------------------------------PART 1:IMPORTING LIBRARIES
import streamlit as st
import numpy as np
import pandas as pd
import os
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go


#streamlit page configuration
st.set_page_config( layout="wide",page_title=None,page_icon=None)

#Streamlit Sidebar
image = Image.open('LOGO2.png')
st.sidebar.image(image)
st.sidebar.title('Healthcare Report')
st.sidebar.markdown("Autistic Spectrum Disorder Screening")
st.sidebar.markdown("Report Prepared By Dalal El Khatib ")
st.sidebar.markdown(" Volunteer Data Analyst at Lebanese Autisim Society ")
st.sidebar.subheader('Dashboard Password')
password=st.sidebar.text_input("Please enter the password", value="", type="password")

def main():
    #------------------------------------PART 2:LOADING AND INSPECTING DATA
    df1 = pd.read_csv('Autism_Data.arff',na_values='?')
    df2 = pd.read_csv('Toddler Autism dataset July 2018.csv',na_values='?')
    #Inspecting first dataframe
    df1.head(10)
    df1["gender"].replace({"f": "Female", "m": "Male"}, inplace=True)
    df1.rename({'jundice': 'Jaundice'}, axis=1, inplace=True)
    df1.info()
    df1.head()
    #Inspcting second dataframe
    df2.head(10)
    df2.info()
    df2["Sex"].replace({"f": "Female", "m": "Male"}, inplace=True)
    df2.head()

    #------------------------------------PART 3:Exploratory Data Analysis
    st.title("**HealthCare Dashboard: Autistic Spectrum Disorder**")
    my_expander = st.beta_expander("GET TO KNOW MORE ABOUT AUTISIM", expanded=False)
    with my_expander:
        image2 = Image.open('definition.jpg')
        st.image(image2)
    st.markdown("<h1 style='text-align: center; color: black;'>General Statistics of ASD in the World</h1>", unsafe_allow_html=True)

    # STATISTIC 1: POURCENTAGE
    data1= df1[df1['Class/ASD']=='YES']
    data2= df2[df2['Class/ASD Traits ']=='Yes']
    my_expander = st.beta_expander("World Prevalence Of Autism Between Toddler and Adults", expanded=False)
    with my_expander:
        st.header("** World Prevalence Of Autism Between Toddler and Adults**")
        text1,figure1 = st.beta_columns(2)
        with text1:
            st.write("Our Sample has shown")
            st.write("Adults: ",len(data1)/len(df1) * 100,"%")
            st.write("Toddlers:",len(data2)/len(df2) * 100,"%")
        with figure1:
            image3 = Image.open('stat1.png')
            st.image(image3)


    # STATISTIC 2: COUNTRY AND ETHNICITY DISTRIBUTION
    my_expander = st.beta_expander("Country Distribution Of Autism Between Toddler and Adults", expanded=False)
    with my_expander:
        st.header("** Country Distribution Of Autism Between Toddler and Adults**")
        figure10,figure11,figure12 = st.beta_columns(3)
        with figure10:
            print(data1['contry_of_res'].value_counts())
            fig5 = go.Figure(data=[go.Table(header=dict(values=['Country Name','Number of Detected ASD'],fill_color='#38B6FF',line_color="black"),
            cells=dict(values=[['United States', 'United Kingdom','New Zealand','Australia','Canada','India','Brazil','France','Netherlands','Malaysia'],[53, 29, 15, 12,10,6,5,5,4,4]],
                 line_color='#000000',fill_color='White'))])
            fig5.update_layout(title_text='Top 10 Countires with ASD',width=370, height=500)
            st.plotly_chart(fig5)
        with figure11:
            st.header("")
            st.header("")
            image4 = Image.open('stat2.png')
            st.image(image4)
        with figure12:
            print(data1['ethnicity'].value_counts())
            fig6 = go.Figure(data=[go.Table(header=dict(values=['Ethnicity','Number of Detected ASD'],fill_color='#38B6FF',line_color="black"),
                 cells=dict(values=[['White-European','Black','Asian','Latino','Middle Eastern'],[109, 18, 16, 10,8]],
                 line_color='#000000',fill_color='White'))])
            fig6.update_layout(title_text='Top 5 Ethnicities with ASD',width=350, height=400)
            st.plotly_chart(fig6)


    # STATISTIC 3: AGE DISTRIBUTION
    my_expander = st.beta_expander("Age Distribution for Autism Toddler and Adults", expanded=False)
    with my_expander:
        st.header("**Age Distribution for Autism Toddler and Adults**")
        figure2,figure3 = st.beta_columns(2)
        with figure2:
            df = px.data.tips()
            fig3 = px.histogram(data1, x='age', nbins=45)
            fig3.layout.plot_bgcolor='#FFFFFF'
            fig3.update_traces(marker_color='#38B6FF',marker_line_color='#000000',marker_line_width=1.5, opacity=1)
            fig3.update_layout(title_text='Age Distribution For Adults',autosize=False,width=500,height=400)
            st.plotly_chart(fig3)
        with figure3:
            fig4 = px.histogram(data2, x='Age_Mons', nbins=30)
            fig4.layout.plot_bgcolor='#FFFFFF'
            fig4.update_traces(marker_color='#38B6FF',marker_line_color='#000000',marker_line_width=1.5, opacity=1)
            fig4.update_layout(title_text='Age Distribution For Toddlers',autosize=False,width=500,height=400)
            st.plotly_chart(fig4)

    #STATISTIC 4: GENDER
    my_expander = st.beta_expander("ASD Distribution Between Gender", expanded=False)
    with my_expander:
        st.header("**ASD Distribution Between Gender**")
        figure4,figure5,figure6 = st.beta_columns(3)
        with figure4:
            image3 = Image.open('stat3.png')
            st.image(image3)
            st.write("One potentially important factor is diagnostic bias: Several studies suggest that girls receive autism diagnoses later in life than boys, indicating that the condition is harder to spot in girls")
        with figure5:
            df = data2.groupby(by=["Sex"]).size().reset_index(name="counts")
            fig3 = px.pie(df, values='counts', names='Sex', hole=.3)
            fig3.update_traces(textposition='inside', textinfo='percent+label',marker=dict(colors=['#D0EDFF', '#38B6FF']))
            fig3.update_layout(showlegend=True)
            st.plotly_chart(fig3, use_column_width=False)
        with figure6:
            st.header("")

    #STATISTIC 5: GENDER AND JUNDICE
    my_expander = st.beta_expander("Is Jaundice a real Indicator of ASD?", expanded=False)
    with my_expander:
        st.header("** Is Jaundice a real Indicator of ASD?**")
        figure7,figure8 = st.beta_columns(2)
        with figure7:
            df = pd.DataFrame({"Jaundice": ["yes", "no"],"gender": ["Male", "Female"]})
            df = data1.groupby(by=["Jaundice", "gender"]).size().reset_index(name="counts")
            color_discrete_map = {'Female': '#D0EDFF','Male':'#38B6FF'}
            fig1=px.bar(data_frame=df, x="Jaundice", y="counts", color="gender", barmode="group",color_discrete_map = color_discrete_map)
            fig1.layout.plot_bgcolor='#FFFFFF'
            fig1.update_layout(title_text='Effect of Jaundice on ASD given Gender for Adults',autosize=False,width=500,height=400)
            st.plotly_chart(fig1)
        with figure8:
            df2 = pd.DataFrame({"Jaundice": ["yes", "no"],"Sex": ["Male", "Female"]})
            df2 = data2.groupby(by=["Jaundice", "Sex"]).size().reset_index(name="counts")
            color_discrete_map = {'Female': '#D0EDFF','Male':'#38B6FF'}
            fig2=px.bar(data_frame=df2, x="Jaundice", y="counts", color="Sex", barmode="group",color_discrete_map = color_discrete_map)
            fig2.layout.plot_bgcolor='#FFFFFF'
            fig2.update_layout(title_text='Effect of Jaundice on ASD given Gender for Toddler',autosize=False,width=500,height=400)
            st.plotly_chart(fig2)

if password=='April2':
    main()
elif password !='April2':
        st.error("Authentication failed. Please verify your password and try again. ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
