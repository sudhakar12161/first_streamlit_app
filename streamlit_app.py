import streamlit

streamlit.title('Our Health Diet')

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍞 Bread, Egg, Avacado 🥑')
streamlit.text('🥣Milk with boost')

streamlit.header('Build your own Fruit Smoothie')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

