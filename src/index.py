from src.requests.my_get import my_get
from src.html.html_parser import Html_parser
from src.tools.config import ROOT_URL
from src.tools.data_prettier import prettier_data
import pprint as pp


def main():

  # get html pages
  data = my_get(ROOT_URL)

  # parsing html for bs4
  parser = Html_parser(data)
  find_block = parser.get_all_vacancies()

  #prettier data out
  prettier_data(find_block)

  