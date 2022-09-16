from flask import Flask
from src.app.middleware.TestMiddleware import Middleware

def RegisterMiddleware(app:Flask):
    app.wsgi_app = Middleware(app.wsgi_app)

