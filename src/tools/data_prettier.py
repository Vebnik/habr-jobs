from functools import reduce


def get_avg_salary(salary: list[str]):
  return f"Средняя ЗП: {reduce(lambda t, v: int(t) + int(v), salary, 0)/len(salary)}"


def prettier_data(data: list[dict]) -> None:

  print(data)

  print('-'*30)
  print(f'Всего было найдено: {len(data)}')
  print('-'*30)

  salary = []

  for i in data:

    if i['salary']['from']: salary.append(i['salary']['from'])

    print(f"{i['title']}")
    print(f"{i['publishedDate']['title']}")
    print(f"{i['salary']['formatted'] or 'No data'}")
    print(f"{i['salaryQualification']['title']}")
    print(f"{' -> '.join([i['title'] for i in i['skills']])}")
    print('-'*30)

  print(get_avg_salary(salary))