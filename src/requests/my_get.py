import requests as req


def my_get(url: str) -> str:

  res = req.get(url)

  return res.text if res.ok else f'Code {res.status_code}'

