class Book:

    def __init__(self, title, author, genre, book_id=None, is_read=False, is_favorite=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_read = is_read
        self.is_favorite = is_favorite
        self.id = book_id

    def __str__(self):
        read_status = "Прочитана" if self.is_read else "Не прочитана"
        fav_status = "В избранном" if self.is_favorite else ""
        return f"{read_status} {fav_status} {self.title} - {self.author} ({self.genre})"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'is_read': self.is_read,
            'is_favorite': self.is_favorite
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            book_id=data['id'],
            is_read=data['is_read'],
            is_favorite=data['is_favorite']
        )
