import datetime
class Article:
    def __init__(self, title, content, category, authors, date):
        self.title = title
        self.content = content
        self._category = category
        self.authors = authors
        self.date = datetime.datetime(*date)
    
    def title_show(self):
        return f'<div>{self.title}<div>'
    
    def content_show(self):
        return f'<div>{self.content}<div>'
    
    def edit_article(self, new_content):
        self.content += new_content

    def authors_show(self):
        return f'<div>{self.authors}<div>'

    def category(self):
        return self._category

    def __lt__(self, other):
        d1 = self.date
        d2 = other.date
        if d1 < d2:
            return True
        return False
    
    def __str__(self, other):
        return f'{self.content}'
    
    def change_date(self, new_date):
        self.date = datetime.datetime(*new_date)

class Author:
    def __init__(self, fname, lname, bio):
        self._fname = fname
        self._lname = lname
        self._bio = bio

    @property
    def fname(self):
        return self._fname
    
    @property
    def lname(self):
        return self._lname
    
    @property
    def bio(self):
        return self._bio

