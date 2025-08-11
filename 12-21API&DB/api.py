from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

@book_blp.route('/')
class Booklist(MethodView):
    @book_blp.resonse(200, BookSchema(many=True))
    def get(self):
        return books
    
    @book_blp.arguments(BookSchema)
    @book_blp.resonse(201, BookSchema)
    def get(self, new_data):
        new_data['id'] = len(books) +1 #북스 리스트의 길이에 +1 값을 더한 수를 id변수에 저장
        books.append(new_data) #리스트에 append한다.
        return new_data
    
@book_blp.route('/<int:book_id>') #유저에게 받은 북 id로 찾아본다.
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def goet(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.") #값이 None이면 없다고하고
        return book #찾으면 찾은값을 반환.
    
    @book_blp.agruments(BookSchema) #유저의 데이터 업데이트 요청
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data) #새로운 데이터로 편집
        return book
    
@book_blp.response(204)
def delete(self, book_id):
    global books #글로벌 선언으로 전역에 선언.
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        abort(404, message="Book not found.")
    books = [book for book in books if book['id'] != book_id]
    return ''