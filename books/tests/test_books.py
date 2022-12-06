from books.requests.books import *


class TestBooks:
    def test_get_books_200(self):
        r = get_books()
        assert r.status_code == 200, 'status code is not ok'

    def test_get_all_books_total(self):
        r = get_books()
        assert len(r.json()) == 6, 'number of books is wrong'

    def test_get_all_books_limit(self):
        r = get_books(limit=3)
        assert len(r.json()) == 3, 'book limit is wrong'

    def test_get_all_books_type(self):
        r = get_books(book_type='non-fiction')
        assert len(r.json()) == 2, 'book type is wrong'

    def test_get_all_books_type_and_limit(self):
        r = get_books(book_type='non-fiction', limit=1)
        assert len(r.json()) == 1, 'book type and limit is wrong'

    def test_get_all_books_invalid_type(self):
        r = get_books(book_type='test')
        assert r.status_code == 400, 'status code not ok'
        assert r.json()[
                   'error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", 'wrong error'

    def test_get_all_books_info(self):
        book = get_books().json()[0]
        expected = {
            "id": 1,
            "name": "The Russian",
            "type": "fiction",
            "available": True
        }
        assert book == expected, 'book info is wrong'

    def test_get_book(self):
        book = get_book(1).json()
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "fiction",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert get_book(1).status_code == 200, 'status code not ok'
        assert book == expected, 'book data is not ok'
