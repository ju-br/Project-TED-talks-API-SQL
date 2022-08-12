import random
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def greeting ():
    return f"How are you doing?"

@app.route("/random-number")
def random_number():
    return str(random.choice(range(0,11)))

    
@app.route("/campus/<location>")
def campus_location (location):
    if location == "bcn":
        return "Carrer Pamplona 96"
    elif location == "mad":
        return "Paseo de la chopera, 14"
    
if __name__ == '__main__':
    app.run()
    
