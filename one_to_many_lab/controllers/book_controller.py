from flask import render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/books')
def books():
    all_book_list = book_repository.select_all()
    return render_template('books/index.html', all_book_list = all_book_list)

@book_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', all_authors=authors)

@book_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']

    author = author_repository.select(author_id)
    book = Book(title, genre, author)
    book_repository.save(book)
    return redirect('/books')
