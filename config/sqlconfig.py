import sqlalchemy as alch
import pymysql
import os
import dotenv

dotenv.load_dotenv()

password = os.getenv('sql_password')
dbName = 'TED' #name of project database
connectionData = f'mysql://root:{password}@localhost/{dbName}'

#connectionData = f"mysql+pymsql://root:{password}@localhost/{dbName}"


engine = alch.create_engine(connectionData)