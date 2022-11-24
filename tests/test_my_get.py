from src.requests.my_get import My_request


TEST_URL = 'https://jsonplaceholder.typicode.com/todos/1'


def test_request():
  request = My_request(TEST_URL)
  response = request.get()

  assert isinstance(response, str)