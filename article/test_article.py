from article import Article
from datetime import datetime
def test_compare():
    article1 = Article('fdfd', 'dfdf', {'war': 1}, [], (2000, 1, 1))
    article2 = Article('fdfd', 'dfdf', {'war': 1}, [], (1999, 1, 1))
    assert article2 < article1

def test_change_date():
    article = Article('fdfd', 'dfdf', {'war': 1}, [], (2000, 1, 1))
    article.change_date((1999, 1, 1))
    assert article.date == datetime(1999, 1, 1)