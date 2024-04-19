from pymongo import MongoClient
from pymongo.server_api import ServerApi
import ssl

uri = "mongodb+srv://22022638:tyV3LKHfGb3qokA5@wordsearch.gceackn.mongodb.net/?retryWrites=true&w=majority&appName=WordSearch"

# Create a new client and connect to the server
try:
    client = MongoClient(uri, ssl=True, server_api=ServerApi('1'))
    
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
