class book:
    def __init__(self, title, author, year):
        self.t = title
        self.a = author
        self.y = year
    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.t,self.a,self.y)  
result = book('Harry Potter', 'J. K. Rowlling', 1997)
print(result.get_info())