from models.author import Author
from models.book import Book

from repositories import author_repository
from repositories import book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author('Revvy')
author_repository.save(author1)
author2 = Author("Bladder Head")
author_repository.save(author2)

book1 = Book("Naked Lunch", "Psy", author1)
book2 = Book("Dobbie", "Love", author2)
book3 = Book("Master of None", "Comedy", author1)
book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)


