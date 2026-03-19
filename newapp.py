import streamlit as st

user_file = st.file_uploader ("Upload your CSV file", type = "CSV")

import pandas as pd
if user_file:
   df = pd.read_csv(user_file)
   st.dataframe(df)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

fig, ax = plt.subplots()
x = ["Total_Credit_Cards"]
y = ["Avg_Credit_Limit"]

plt.scatter(x, y)
sns.scatterplot(data = df, )
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Total Credit Card Versus Average Credit Limit")

plt.show()
st.pyplot(fig)