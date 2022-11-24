from functools import reduce


def data_prettier(data: list[dict]):

  
  def _print(i):
    print(f"{i['title']}")
    print(f"{i['publishedDate']['title']}")
    print(f"{i['salary']['formatted'] or 'No data'}")
    print(f"{i['salaryQualification']['title']}")
    print(f"{' -> '.join([i['title'] for i in i['skills']])}")
    print('-'*30)
    return


  def _print_sum(data):
    print('-'*30)
    print(f'Всего было найдено: {len(data)}')
    print('-'*30)
    return


  def get_avg_salary(salary: list[str]):
    return f"Средняя ЗП: {reduce(lambda t, v: int(t) + int(v), salary, 0)/len(salary)}"


  def prettier(data: list[dict]) -> None:
    
    salary = []

    _print_sum(data)

    for i in data:
      if i['salary']['from']: 
        salary.append(i['salary']['from'])

      _print(i)

    print(get_avg_salary(salary))


  prettier(data)

