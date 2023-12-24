import requests
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg

try:
  response = requests.get('https://nodejs.org/en/')
  soup = BeautifulSoup(response.content, 'html.parser')
  downloadBtn = soup.find('a', class_ = 'home-downloadbutton')
  buttonText = downloadBtn.text
  msg = buttonText
  title = 'Current NodeJS version'
except ConnectionError:
  msg = 'Internet connection lost'
  title = 'Network error'

dpg.create_context()
dpg.create_viewport(title = title, width = 300, height = 150)
dpg.setup_dearpygui()

with dpg.window(tag = 'Primary'):
 dpg.add_text(msg)

dpg.show_viewport()
dpg.set_primary_window('Primary', True)
dpg.start_dearpygui()
dpg.destroy_context()
