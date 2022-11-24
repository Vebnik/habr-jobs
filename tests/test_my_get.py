from src.requests.my_get import my_get


TEST_URL = 'https://career.habr.com/vacancies?qid=3&skills%5B%5D=446&type=all'


def test_request():
  data = my_get(TEST_URL)

  print('data')

  assert isinstance(data, str)
