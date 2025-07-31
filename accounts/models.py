from django.db import models
from mongoengine import Document, StringField, EmailField

# Create your models here.

class User(Document):
    ## the following lines can be said to be Schema of our Database 
    username = StringField(required=True, unique=True, max_length=30)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
