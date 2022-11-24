from src.html.html_parser import Html_parser


TEST_HTML = '<script>PLACE</script><script>{"vacancies":{"list": true}}</script><script>PLACE</script>'


def test_html_parser():
  pars = Html_parser(TEST_HTML)
  result = pars.get_all_vacancies()

  assert result