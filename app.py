from dotenv import load_dotenv
import os
from flask import Flask, render_template
from pymongo import MongoClient
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER  = os.getenv('MONGODB_CLUSTER')

app = Flask(__name__)

# Conexión a MongoDB Atlas
#client = MongoClient('mongodb+srv://mpoma:Universo789$@mycluster789.mdxep.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster789')
client = MongoClient(f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/?retryWrites=true&w=majority&appName=MyCluster789')
db = client.shop_db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_collection = db.products
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)