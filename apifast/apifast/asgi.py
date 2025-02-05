# myproject/asgi.py

import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from .api import app as fastapi_app
from fastapi import FastAPI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apifast.settings')


# django_app = get_asgi_application()
# app = FastAPI()

# app.mount("/", WSGIMiddleware(django_app))
django_app = get_asgi_application()
app = WSGIMiddleware(django_app)
app.mount("/api", fastapi_app)

# import os
# from django.core.asgi import get_asgi_application
# from fastapi.middleware.wsgi import WSGIMiddleware
# from fastapi import FastAPI
# from .api import app as fastapi_app  # Assuming this is your FastAPI app

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apifast.settings')

# # Initialize the Django ASGI application
# django_app = get_asgi_application()

# # Create a new FastAPI app
# app = FastAPI()

# # Mount the Django application to the FastAPI app
# app.mount("/", WSGIMiddleware(django_app))

# # Mount your FastAPI routes under "/api"
# app.mount("/api", fastapi_app)
