import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


with open("db_credential.json", "r") as db_info_file:
    db_data = json.load(db_info_file)
    
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_data['USER']}:{db_data['PASSWORD']}@{db_data['HOST']}:{db_data['PORT']}/{db_data['DB_NAME']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()