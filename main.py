from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import json
import random
import tools.sqltools as sql
import pymysql

app = Flask(__name__)

# GET: render markdown
@app.route("/")
def hola ():
    return 'hola'

'''
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template
'''

# Get everything: SQL
@app.route("/Talks/")
def all_talks ():
    return jsonify(sql.get_everything())

# Get everything FROM sentiment: SQL & argument
@app.route("/Talks/<sentiment>")
def talk_speaker (sentiment):
    return jsonify(sql.get_everything_from_sentiment(sentiment))

    # Get everything FROM year: SQL & argument
@app.route("/Talks/<year>")
def talk_year (year):
    return jsonify(sql.get_everything_from_year(year))




## POST
@app.route("/Talks", methods=["POST"])
def insert_message():

    database = request.args["db"]

    if database == "mongo":
        pass


    elif database == "sql":
        talk = request.form.get("title")
        speaker = request.form.get("speaker")
        description = request.form.get("description")
        year = request.form.get("year")
        return sql.new_message(talk, speaker, description,year)

    else:
        return "You need to include the db param: either mongo or sql"


app.run(port=5000, debug=True)