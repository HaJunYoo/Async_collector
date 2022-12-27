from odmantic import Model

class BookModel(Model):
    keyword: str
    publisher: str
    link: str
    image: str

    # collection name을 여기서 지정가능
    class Config:
        collection = "books"

# db(fastapi-pj) -> collection(books) -> document {
# keyword : ~~~
# }