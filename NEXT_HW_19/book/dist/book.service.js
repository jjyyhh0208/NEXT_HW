"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BookService = void 0;
class BookService {
    constructor() {
        this.books = [];
    }
    getAllBooks() {
        return this.books;
    }
    createBook(BookDto) {
        const id = this.books.length + 1;
        this.books.push({ id: id.toString(), ...BookDto, createdDt: new Date() });
    }
    getBook(id) {
        const Book = this.books.find((Book) => {
            return Book.id === id;
        });
        console.log(Book);
        return Book;
    }
    delete(id) {
        const filteredBooks = this.books.filter((Book) => Book.id !== id);
        this.books = [...filteredBooks];
    }
    updateBook(id, BookDto) {
        let updateIndex = this.books.findIndex((Book) => Book.id === id);
        const updateBook = { id, ...BookDto, updatedDt: new Date() };
        this.books[updateIndex] = updateBook;
        return updateBook;
    }
}
exports.BookService = BookService;
//# sourceMappingURL=book.service.js.map