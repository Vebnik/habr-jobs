import requests as req


class My_request:

  url = None

  def __init__(self, url) -> None:
    self.url = url


  def get(self):
    res = req.get(self.url)
    return res.text if res.ok else f'Code {res.status_code}'


  def post(self, data) -> str:
    res = req.post(self.url, data)
    return res.text if res.ok else f'Code {res.status_code}'


