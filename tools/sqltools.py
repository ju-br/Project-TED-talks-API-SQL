from config.sqlconfig import engine
import pandas as pd

## GET
def get_everything ():

    query = (f"""SELECT * FROM Talks;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_everything_from_sentiment(sentiment):

    query = (f"""SELECT * FROM Talks WHERE sentiment = "{sentiment}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_everything_from_year(year):

    query = (f"""SELECT * FROM Talks WHERE year = "{year}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## POST
def new_message (title, speaker, description,year):

    engine.execute(f"""
    INSERT INTO users (title, speaker, description,year)
    VALUES ({title}, '{speaker}', '{description}','{year}');
    """)
    
    return f"Correctly introduced: {title} {speaker} {description} {year}"