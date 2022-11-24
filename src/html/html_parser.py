import bs4
import json


class Html_parser:

  data = None
  soup = bs4.BeautifulSoup


  def __init__(self, data: str) -> None:
    self.data = data
    self.soup = bs4.BeautifulSoup(data, 'html.parser')


  def get_all_vacancies(self) -> list[str]:
    try:
      result = self.soup.find_all('script')
      return json.loads(result[1].get_text())['vacancies']['list']
    except:
      print('Error in get_all_vacancies')
      exit()


  def get_all_link(self) -> list[str]:
    pass