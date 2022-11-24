from src.requests.my_get import My_request
from src.html.html_parser import Html_parser
from src.tools.config import ROOT_URL
from src.tools.data_prettier import data_prettier
import jmespath as jms
import re


def main():

  # get html pages
  req = My_request(ROOT_URL)
  data = req.get()

  # parsing html for bs4
  parser = Html_parser(data)
  find_block = parser.get_all_vacancies()

  # prettier data out
  data_prettier(find_block)

