import streamlit
import requests
import snowflake.connector
import pandas as pd
from urllib.error import URLError


streamlit.title('Our Health Diet')

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍞 Bread, Egg, Avacado 🥑')
streamlit.text('🥣Milk with boost')

streamlit.header('Build your own Fruit Smoothie')



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvise_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('WHat fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvise_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
streamlit.stop() 
streamlit.header("Fruityvise Fruit Advise!")
fruit_entered = streamlit.text_input('What fruit would you like to add?')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()

streamlit.dataframe(my_data_rows)


streamlit.write('Thanks for adding: ',fruit_entered)

my_cur.execute("insert into fruit_load_list values")






