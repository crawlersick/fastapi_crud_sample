from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .internal.settings import Settings

SQLALCHEMY_DATABASE_URL = Settings().db1url
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
print("hihihihihihihihihihihihihi============")
print(Settings().ENVIRONMENT)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

