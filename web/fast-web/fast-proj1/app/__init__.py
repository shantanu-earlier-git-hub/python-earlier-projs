from app.routes.author_routes import author_router
from app.routes.books_routes import books_router
from app.routes.store_routes import store_router

from .dependencies import app

app.include_router(books_router)
app.include_router(author_router)

app.include_router(store_router)
