
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, String, Date



SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

user = 'root'
password = 'Shiva12*'
host = 'localhost'
database = 'demo'

connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

engine = create_engine(connection_string)

metadata = MetaData()


customerData = Table('customerData', metadata,
    Column('Name', String(50)),
    Column('email_address', String(40)),
    Column('phone_no', String(20)),
    Column('state', String(20)),
    Column('country', String(20)),
    Column('DOB', Date)
)

metadata.create_all(engine)
