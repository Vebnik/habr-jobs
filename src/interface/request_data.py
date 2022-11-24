from dataclasses import dataclass


@dataclass
class Request_data:
  headers: dict
  params: dict
  data: dict