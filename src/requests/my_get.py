import requests as req
from src.interface.request_data import Request_data


class My_request:

  url: str = None

  def __init__(self, url: str) -> None:
    self.url = url


  def get(self) -> str:
    res = req.get(self.url)
    return res.text if res.ok else f'Code {res.status_code}'


  def post(self, data: Request_data) -> str:
    res = req.post(self.url, data=data.data, headers=data.headers, params=data.params)
    return res.text if res.ok else f'Code {res.status_code}'

