import streamlit
import requests


streamlit.title('Our Health Diet')

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍞 Bread, Egg, Avacado 🥑')
streamlit.text('🥣Milk with boost')

streamlit.header('Build your own Fruit Smoothie')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Raspberry)
streamlit.text(fruityvice_response)
