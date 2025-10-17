from sqlalchemy import Column, Integer, String
from database import Base  # import the Base from Step 1

class User(Base):
    __tablename__ = "users"  # this will be your table name in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # primary key column
    name = Column(String, nullable=False)  # name column, cannot be empty
    email = Column(String, unique=True, index=True, nullable=False)  # email column, must be unique
