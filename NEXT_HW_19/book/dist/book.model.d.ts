export interface BookDto {
    id: string;
    title: string;
    author: string;
    publishedDt?: Date;
    isAvailable: boolean;
}
