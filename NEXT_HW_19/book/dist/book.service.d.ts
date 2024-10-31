import { BookDto } from './book.model';
export declare class BookService {
    books: any[];
    getAllBooks(): any[];
    createBook(BookDto: BookDto): void;
    getBook(id: any): any;
    delete(id: any): void;
    updateBook(id: any, BookDto: BookDto): {
        updatedDt: Date;
        id: string;
        title: string;
        author: string;
        publishedDt?: Date;
        isAvailable: boolean;
    };
}
