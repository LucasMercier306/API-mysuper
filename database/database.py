from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

postgres_url = os.environ.get('POSTGRES_URL')
postgres_port = os.environ.get('POSTGRES_PORT=5432')
postgres_db = os.environ.get('POSTGRES_DB')
postgres_user = os.environ.get('POSTGRES_USER')
postgres_pwd = os.environ.get('POSTGRES_PWD')


# SQLALCHEMY_DATABASE_URL = f"postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_user}:{postgres_pwd}@{postgres_url}/{postgres_db}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()