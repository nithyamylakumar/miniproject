import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")

st.title("ICA 5 STREAMLIT WEBAPP FOR HEART DISEASE DATASET", anchor = None)

st.title("Different types of visualisation using Seaborn")

str_text = ':Data-set information: \n - - This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. \n  - In particular, the Cleveland database is the only one that has been used by ML researchers to this date. \n - The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. \n Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0). \n  - The names and social security numbers of the patients were recently removed from the database, replaced with dummy values. \n The 14 attrbutes used are as follows: \n 1. age \n 2. sex \n 3. cp \n 4. trestbps \n 5. chol \n 6.fbs \n 7.restecg \n 8.thalach \n 9. exang \n 10. oldpeak \n 11. slope \n 12. ca \n 13. thal \n 14. num'


st.text(str_text)
#df1 = df.drop(['Unnamed: 32'],axis = 1)

df.describe()

x = df.columns.tolist()
y = df.columns.tolist()

st.title("SCATTER PLOT")
x_axis_3 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 3)
y_axis_4= st.selectbox(label = "Select an attribute for  y axis", options = y, key = 4)
plt.figure(figsize = (6,5))
img_3 = sns.scatterplot(data = df, x = x_axis_3, y= y_axis_4, hue = 'ca', legend = 'full')
st.pyplot(img_3.figure)

'''
st.title("CATPLOT")
x_axis_5 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 5)
y_axis_6 = st.selectbox(label = "Select an attribute for  y axis", options = y, key = 6)
plt.figure(figsize = (6,5))
img_4 = sns.catplot(data=df1, x=x_axis_5, y=y_axis_6, hue = 'diagnosis')
st.pyplot(img_4)


x_axis_1 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 1)
plt.figure(figsize = (6,5))
img_1 = sns.displot(df1, x= x_axis_1, hue = 'diagnosis', multiple = 'dodge')
st.pyplot(img_1)


st.title("DISPLOT- KDE")
x_axis_2= st.selectbox(label = "Select an attribute for x axis", options = x, key = 2)
plt.figure(figsize = (6,5))
img_2 = sns.displot(df1, x=x_axis_2, hue="diagnosis", kind="kde")
st.pyplot(img_2)



st.title("VIOLINPLOT")
x_axis_7 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 7)
y_axis_8 = st.selectbox(label = "Select an attribute for y axis", options = y, key = 8)
plt.figure(figsize = (6,5))
img_5 = sns.catplot(data = df1, x = x_axis_7, y = y_axis_8, kind = 'violin', hue = 'diagnosis')
st.pyplot(img_5)



st.title('REGRESSION PLOT', anchor = None)
x_axis_9 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 9)
y_axis_10 = st.selectbox(label = "Select an attribute for y axis", options = y, key = 10)
plt.figure(figsize = (6,5))
img_6 = sns.regplot(data= df1, x = x_axis_9, y = y_axis_10)
st.pyplot(img_6.figure)


st.title('JOINT PLOT', anchor = None)
x_axis_11 = st.selectbox(label = "Select an attribute for x axis", options = x, key = 11)
y_axis_12 = st.selectbox(label = "Select an attribute for y axis", options = y, key = 12)
plt.figure(figsize = (6,5))
img_7 = sns.jointplot(x=x_axis_11, y=y_axis_12, data=df1, kind = 'reg')
st.pyplot(img_7)


st.title('PAIRPLOT', anchor = None)
a  = st.selectbox(label = "Select a feature of choice", options = x, key = 13)
b  = st.selectbox(label = " Select a feature of choice" , options = x, key = 14)
c  = st.selectbox(label = " Select a feature of choice", options = x, key = 15)
plt.figure(figsize = (6,5))
img_8 = sns.pairplot(data= df1, x_vars = [a,b,c], y_vars = [a,b,c], hue = 'diagnosis')
st.pyplot(img_8)

'''


















