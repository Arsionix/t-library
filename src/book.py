class Book:

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_read = False
        self.is_favorite = False
        self.id = None

    def __str__(self):
        read_status = "Прочитана" if self.is_read else "Не прочитана"
        fav_status = "В избранном" if self.is_favorite else ""
        return f"{read_status} {fav_status} {self.title} - {self.author} ({self.genre})"
