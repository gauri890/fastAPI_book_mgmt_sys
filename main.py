from fastapi import Body, FastAPI

app = FastAPI()

Books = [
    {
     "book_id" : 1,
     "title" : "title 1",
     "auther_name": "abc 1",
     "category":"thriller"
    },
    {
     "book_id" : 2,
     "title" : "title 1",
     "auther_name": "efg 3",
     "category":"crime"
    }
]

book1 = {
    "book_id" : 2,
    "title" : "title 2",
    "auther_name": "cde 2",
    "category":" romance"
}

# root endpoint
@app.get("/")
async def get_root_method():
    return {"message": "Welcome Home"}

#get all books endpoint
@app.get("/books")
async def get_all_books():
    return Books

#get books by book_id endpoint
@app.get("/books/{book_id}")
async def get_book(book_id:int):
    for book in Books:
        if book.get("book_id") == book_id:
            return book
    return {"message": "Nothing found"}

#query parameter 
@app.get("/books/")
async def get_book(category:str):
    books_to_return = []
    for book in Books:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Using both path and query parameter
@app.get("/books/{book_title}")
async def get_book(book_title:str,category:str):
    books_to_return = []
    for book in Books:
        if book.get("title").casefold() == book_title.casefold():
            if book.get("category").casefold() == category.casefold():
                return books_to_return.append(book)
    return {"message": "Nothing found"}

#post endpoint for new_book body
@app.post("/books/")
async def post_book(new_book=Body()):
    Books.append(new_book)
    return Books

@app.put("/books/{book_id}")
async def put_book(book_id:int):
    
    return Books

@app.delete("/books/{book_id}")
async def delete_book(book_id:int):
    return Books