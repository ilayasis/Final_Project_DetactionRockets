from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from django.conf import settings

# Create a connection pool
client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], maxPoolSize=10)

# Test the connection
try:
    client.admin.command('ping')
    print('Connected to MongoDB')
except ConnectionFailure:
    print('Failed to connect to MongoDB')