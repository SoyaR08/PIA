class Libro:
    def __init__(self, title, autor, num_pag, publish_year):
        self.title = title
        self.autor = autor
        self.num_pag = num_pag
        self.publish_year = publish_year

    def __str__(self):
        return f"'{self.title}' de {self.autor}, {self.num_pag} páginas, publicado en {self.publish_year}."
    
    def isLarge(self):
        return "Es corto" if self.num_pag < 300 else "Es largo"
        
